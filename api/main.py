from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import sqlite3
import os
from llm.query_llm import question_to_sql
from visualizer.charts import generate_bar_chart, generate_pie_chart

app = FastAPI()
app.mount("/charts", StaticFiles(directory="charts"), name="charts")
templates = Jinja2Templates(directory="templates")

class Question(BaseModel):
    question: str

@app.get("/", response_class=HTMLResponse)
async def get_home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/ask")
async def ask(q: Question):
    try:
        sql_query = question_to_sql(q.question)
        print(f"Generated SQL: {sql_query}")

        conn = sqlite3.connect("data/ecommerce.db")
        cursor = conn.cursor()
        cursor.execute(sql_query)
        result = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        conn.close()

        # Format single value response
        if len(columns) == 1 and len(result) == 1:
            value = result[0][0]
            response_text = f" Answer is: ₹{value:,.2f}"
            return {
                "columns": columns,
                "result": result,
                "message": response_text
            }

        # Generate chart for two-column results
        elif len(columns) == 2 and len(result) > 1:
            if "share" in q.question.lower() or "percentage" in q.question.lower() or "distribution" in q.question.lower():
                chart_path = generate_pie_chart(columns, result, title="Data Distribution")
            else:
                chart_path = generate_bar_chart(columns, result, title="Data Breakdown")

            return {
                "columns": columns,
                "result": result,
                "chart": chart_path,
                "message": f" Chart created: {chart_path}"
            }

        else:
            return {
                "columns": columns,
                "result": result
            }

    except Exception as e:
        return {"error": str(e)}
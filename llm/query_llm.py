import google.generativeai as genai

genai.configure(api_key="AIzaSyB90TP-Sm99M8cDWt-fsTn6U6lH9kV8-NQ")

model = genai.GenerativeModel("models/gemini-1.5-flash")




def question_to_sql(question: str) -> str:
    prompt = f"""
You are a helpful assistant that converts natural language into SQL.

Use these tables:
- AdSales(ad_sales, impressions, clicks, item_id, date)
- TotalSales(total_sales, item_id, date)
- Eligibility(item_id, is_eligible, reason)

Now convert this question to SQL: {question}

Only return the SQL query. No explanation.
"""
    response = model.generate_content(prompt)
    sql = response.text.strip()

    # ✅ Remove markdown formatting if present
    if sql.startswith("```sql"):
        sql = sql.replace("```sql", "").replace("```", "").strip()

    return sql

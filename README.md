# GenAI-Intern-VIT-Chennai

**
This is a website that lets you ask questions about your e-commerce data in simple words. It gives answers as text, tables, or charts by using AI and a local database.**



To run the project in website use this command:
    "uvicorn api.main:app --reload"

to install all the necessary libraries:
pip install openai python-dotenv fastapi uvicorn pandas matplotlib google-generativeai jinja2 python-dotenv


Questions solved:
1."What is my total sales?"                                                                                                                  
2."Show total sales by item"                                                                                             
→ bar chart (displayed in charts folder)                                                                                                                                      
3."What is the percentage share of total sales by item?"                                                                                                       
→ pie chart (displayed in charts folder)                                                                                                    

import pandas as pd
import sqlite3

conn = sqlite3.connect("data/ecommerce.db")

pd.read_csv("data/ad_sales.csv").to_sql("AdSales", conn, if_exists="replace", index=False)
pd.read_csv("data/total_sales.csv").to_sql("TotalSales", conn, if_exists="replace", index=False)
pd.read_csv("data/eligibility.csv").to_sql("Eligibility", conn, if_exists="replace", index=False)

print("Tables created successfully.")
conn.close()

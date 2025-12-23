import pandas as pd
import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1234",
    database="amazon_sales_analysis"
)
cursor = connection.cursor()

products_df = pd.read_csv("C:\\Users\FAZAL\\Documents\\Final Project\\Amazon Sale Analysis\\products_df.csv")

insert_sql = """
INSERT INTO products (order_id, sku, size, asin, style, category)
VALUES (%s, %s, %s, %s, %s, %s)
"""

for row in products_df.itertuples(index=False):
    cursor.execute(insert_sql, row)

connection.commit()
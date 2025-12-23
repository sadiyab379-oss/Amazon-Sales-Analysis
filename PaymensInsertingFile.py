import pandas as pd
import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1234",
    database="amazon_sales_analysis"
)
cursor = connection.cursor()

payments_df = pd.read_csv("C:\\Users\FAZAL\\Documents\\Final Project\\Amazon Sale Analysis\\payments.csv")

payments_df['amount'] = payments_df['amount'].replace('', None)

payments_df = payments_df.fillna('')


insert_sql = """
INSERT IGNORE INTO payments (order_id,qty,currency,amount)
VALUES (%s, %s, %s, %s)
"""


for row in payments_df.itertuples(index=False):
    cursor.execute(insert_sql, row)
connection.commit()







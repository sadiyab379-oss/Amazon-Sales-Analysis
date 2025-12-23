import mysql.connector
import numpy as np
import pandas as pd

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1234",
    database="amazon_sales_analysis"
)
cursor = connection.cursor()

orders_df = pd.read_csv("C:\\Users\\FAZAL\\Documents\\Final Project\\Amazon Sale Analysis\\Orders.csv")

orders_df['Date'] = pd.to_datetime(orders_df['Date'], dayfirst=True).dt.strftime('%Y-%m-%d')

orders_df = orders_df.fillna('')
orders_sql = """
INSERT INTO ORDERS
(order_id,index1,Date,status,fulfilment,sales_channel,ship_service_level,style,promotion_ids,b2b,fulfilled_by)
VALUES (%s, %s, %s, %s, %s, %s,%s, %s, %s, %s,%s)
"""
for row in orders_df.itertuples(index=False):
    cursor.execute(orders_sql, row)
connection.commit()


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

promotions_df = pd.read_csv("C:\\Users\\FAZAL\\Documents\\Final Project\\Amazon Sale Analysis\\promotions.csv")

promotions_df = promotions_df.fillna('')

insert_sql = """
INSERT INTO promotions (order_id,sales_channel,promotion_ids)
VALUES (%s, %s, %s)
"""

for row in promotions_df.itertuples(index=False):
    cursor.execute(insert_sql, row)
connection.commit()

import pandas as pd
import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1234",
    database="amazon_sales_analysis"
)
cursor = connection.cursor()

shipping_df = pd.read_csv("C:\\Users\FAZAL\\Documents\\Final Project\\Amazon Sale Analysis\\shipping.csv")

shipping_df = shipping_df.fillna('')

insert_sql = """
INSERT IGNORE INTO shipping (order_id,ship_city,ship_state,ship_postal_code,ship_country,courier_status)
VALUES (%s,%s,%s,%s,%s,%s)
"""

for row in shipping_df.itertuples(index=False):
    cursor.execute(insert_sql, row)

connection.commit()
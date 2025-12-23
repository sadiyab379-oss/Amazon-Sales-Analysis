import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1234",
    database="amazon_sales_analysis"
)
cursor = connection.cursor()

#1
'''query = """
SELECT status, COUNT(*) AS total_orders
FROM orders
GROUP BY status
"""
df = pd.read_sql(query, connection)

plt.figure()
plt.bar(df['status'], df['total_orders'])
plt.xlabel("Order Status")
plt.ylabel("Total Orders")
plt.title("Orders Status Wise Analysis")
plt.xticks(rotation=45)
plt.show()'''

#2
'''query = """
SELECT fulfilled_by, COUNT(*) AS total_orders
FROM orders
GROUP BY fulfilled_by
"""
df = pd.read_sql(query, connection)

plt.figure()
plt.pie(df['total_orders'], labels=df['fulfilled_by'], autopct='%1.1f%%')
plt.title("Fulfillment Type Distribution")
plt.show()'''

#3
'''query = """ 
SELECT category, COUNT(*) AS total_products 
FROM products 
GROUP BY category 
"""
df = pd.read_sql(query, connection)

plt.figure(figsize=(8, 8))
plt.pie(df['total_products'], labels=df['category'], autopct='%1.1f%%', pctdistance=0.85, wedgeprops=dict(width=0.5))
plt.title("Category Wise Products")
plt.show()'''



#4
'''query = """ 
SELECT category, size, COUNT(*) AS total_products 
FROM products 
GROUP BY category, size 
"""
df = pd.read_sql(query, connection)

# Pivot the data for stacked bar chart
pivoted_df = df.pivot(index='category', columns='size', values='total_products')

plt.figure(figsize=(10, 6))
pivoted_df.plot(kind='bar', stacked=True)
plt.xlabel("Category")
plt.ylabel("Total Products")
plt.title("Category Wise Products by Size")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()'''


#5
'''query = """
SELECT size, COUNT(*) AS total_orders
FROM products
GROUP BY size
"""
df = pd.read_sql(query, connection)

plt.figure()
plt.bar(df['size'], df['total_orders'])
plt.xlabel("Size")
plt.ylabel("Total Orders")
plt.title("Size Wise Sales Analysis")
plt.show()'''

#6
'''query = """ 
SELECT ship_city, courier_status, COUNT(*) AS total_orders 
FROM shipping 
GROUP BY ship_city, courier_status 
ORDER BY ship_city, total_orders DESC 
"""
df = pd.read_sql(query, connection)

# Pivot the data for stacked bar chart
pivoted_df = df.pivot(index='ship_city', columns='courier_status', values='total_orders')

plt.figure(figsize=(12, 8))
pivoted_df.plot(kind='bar', stacked=True)
plt.xlabel("City")
plt.ylabel("Total Orders")
plt.title("City-wise Orders by Courier Status")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()'''


#7
'''query = """ 
SELECT courier_status, COUNT(*) AS total_orders 
FROM shipping 
GROUP BY courier_status 
"""
df = pd.read_sql(query, connection)

plt.figure(figsize=(8, 8))
plt.pie(df['total_orders'], labels=df['courier_status'], autopct='%1.1f%%', pctdistance=0.85, wedgeprops=dict(width=0.5))
plt.title("Courier Status Distribution")
plt.show()'''


#8
'''query = """
SELECT 
    CASE 
        WHEN promotion_ids IS NULL OR promotion_ids = '' THEN 'No Promotion'
        ELSE 'With Promotion'
    END AS promo_type,
    COUNT(*) AS total_orders
FROM orders
GROUP BY promo_type
"""
df = pd.read_sql(query, connection)

plt.figure()
plt.pie(df['total_orders'], labels=df['promo_type'], autopct='%1.1f%%')
plt.title("Promotion Impact on Orders")
plt.show()'''

#9
'''query = """
SELECT SUBSTRING(Date,1,7) AS month, COUNT(*) AS total_orders
FROM orders
GROUP BY month
ORDER BY month
"""
df = pd.read_sql(query, connection)

plt.figure()
plt.plot(df['month'], df['total_orders'], marker='o')
plt.xlabel("Month")
plt.ylabel("Total Orders")
plt.title("Monthly Orders Trend")
plt.xticks(rotation=45)
plt.show()'''


#10
'''query = """
SELECT status, COUNT(*) AS total_orders
FROM orders
GROUP BY status
"""

df = pd.read_sql(query, connection)


# Pie chart
plt.figure(figsize=(7,7))
plt.pie(
    df['total_orders'],
    labels=df['status'],
    autopct='%1.1f%%',
    startangle=140
)

plt.title("Order Status Wise Distribution")
plt.show()'''
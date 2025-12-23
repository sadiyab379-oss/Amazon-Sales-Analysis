-- ANALYSIS
USE amazon_sales_analysis;
-- 1 Total Orders Count
SELECT COUNT(*) AS total_orders
FROM orders;

-- 2 Orders Status Wise Analysis
SELECT status, COUNT(*) AS  total_orders
FROM orders
GROUP BY status
ORDER BY  total_orders DESC;

-- 3 Sales Channel Wise Orders
SELECT sales_channel, COUNT(*) AS  total_orders
FROM orders
GROUP BY sales_channel;

-- 4 Fulfillment Type Analysis
SELECT fulfilled_by, COUNT(*) AS  total_orders
FROM orders
GROUP BY fulfilled_by;

-- 5 Top Selling Products (sku wise)
SELECT 
    p.sku,
    COUNT(*) AS  orders_id
FROM products p
GROUP BY p.sku
ORDER BY orders_id DESC
LIMIT 10;

-- 6 Category-wise Product Count
SELECT category, COUNT(*) AS total_products
FROM products
GROUP BY category
ORDER BY total_products DESC;


-- 7 Size-wise Sales Analysis
SELECT size, COUNT(*) AS total_orders
FROM products
GROUP BY size
ORDER BY total_orders DESC;

-- 8 City-wise Shipping Analysis
SELECT ship_city, COUNT(*) AS total_orders
FROM shipping
GROUP BY ship_city
ORDER BY total_orders DESC;

-- 9 Courier Status Analysis
SELECT courier_status, COUNT(*) AS total_orders
FROM shipping
GROUP BY courier_status;

-- 10 Average Order value
SELECT AVG(amount) AS avg_order_value
FROM payments;

-- 11 Quantity Sold Analysis
SELECT SUM(qty) AS total_quantity_sold
FROM payments;

-- 12 Promotin Impact Analysis
SELECT COUNT(*) AS promoted_orders
FROM orders
WHERE promotion_ids IS NOT NULL
AND promotion_ids <> '';

-- 13 Orders Without Promotion
SELECT COUNT(*) AS non_promoted_orders
FROM orders
WHERE promotion_ids IS NULL
OR promotion_ids = '';

-- 14 Order-wise Complete Sales View (JOIN)
SELECT 
    o.order_id,
    o.status,
    p.sku,
    p.category,
    s.ship_city,
    pay.amount,
    pay.currency
FROM orders o
JOIN products p ON o.order_id = p.order_id
JOIN shipping s ON o.order_id = s.order_id
JOIN payments pay ON o.order_id = pay.order_id;

-- 15 Monthly Orders Trend
SELECT 
 SUBSTRING(Date, 1, 7) AS month,
COUNT(*) AS total_orders
FROM orders
GROUP BY month
ORDER BY month;


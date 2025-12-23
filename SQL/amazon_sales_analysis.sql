CREATE DATABASE amazon_sales_analysis;
USE amazon_sales_analysis;
-- for writing the comments we will use the -- symbol or else we can also use the # simbol
# this is also one type of comment in sql
CREATE TABLE orders(
order_id BIGINT PRIMARY KEY,
Index1 INT ,
Date VARCHAR(50),
status VARCHAR(100),
fulfilment VARCHAR(50),
sales_channel VARCHAR(50),
ship_service_level VARCHAR(100),
style VARCHAR(50),
promotion_ids VARCHAR(3500),
b2b BOOLEAN,
fulfilled_by VARCHAR(50)
);
SELECT * FROM amazon_sales_analysis.orders;

CREATE TABLE products(
product_id INT AUTO_INCREMENT PRIMARY KEY,
order_id BIGINT,
sku VARCHAR(50) ,
size VARCHAR(50),
asin VARCHAR(50),
style VARCHAR(50) UNICODE NOT NULL,
category VARCHAR(50)
);
SELECT * FROM amazon_sales_analysis.products;

CREATE TABLE shipping(
shipping_id	INT AUTO_INCREMENT PRIMARY KEY,
order_id BIGINT,
ship_city VARCHAR(50),
ship_state VARCHAR(50),
ship_postal_code INT,
ship_country VARCHAR(50),
courier_status VARCHAR(50) UNIQUE NOT NULL
);

SELECT * FROM amazon_sales_analysis.shippings;


CREATE TABLE payments(
payment_id	INT AUTO_INCREMENT PRIMARY KEY,
order_id BIGINT,
Qty INT,
currency VARCHAR(5),
amount DECIMAL(20,2)
);
SELECT * FROM amazon_sales_analysis.shippings;

CREATE TABLE promotions(
promotion_id INT AUTO_INCREMENT PRIMARY KEY,
order_id BIGINT,
sales_channel VARCHAR(50),
promotion_ids VARCHAR(3500)
);

SELECT * FROM amazon_sales_analysis.promotions;


USE amazon_sales_analysis;
ALTER TABLE products
ADD CONSTRAINT fk_products_order
FOREIGN KEY (order_id)
REFERENCES orders(order_id);

ALTER TABLE shipping
ADD CONSTRAINT fk_shipping_order
FOREIGN KEY (order_id)
REFERENCES orders(order_id);

ALTER TABLE payments
ADD CONSTRAINT fk_payments_order
FOREIGN KEY (order_id)
REFERENCES orders(order_id);

ALTER TABLE promotions
ADD CONSTRAINT fk_promotions_order
FOREIGN KEY (order_id)
REFERENCES orders(order_id);
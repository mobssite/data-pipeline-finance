-- Create clean table
CREATE TABLE sales_clean AS
SELECT
    date,
    store,
    item,
    sales
FROM sales_raw;

-- KPI queries
-- Revenue per month
SELECT
    strftime('%Y-%m', date) as month,
    SUM(sales) as total_sales
FROM sales_clean
GROUP BY month;

-- Top stores
SELECT
    store,
    SUM(sales) as total_sales
FROM sales_clean
GROUP BY store
ORDER BY total_sales DESC;
-- Revenue total
SELECT SUM(sales) as total_revenue
FROM sales_raw;
-- Revenue par mois
SELECT 
    strftime('%Y-%m', date) as month,
    SUM(sales) as revenue
FROM sales_raw
GROUP BY month
ORDER BY month;
-- Top clients
SELECT 
    customer_id,
    SUM(sales) as total_spent
FROM sales_raw
GROUP BY customer_id
ORDER BY total_spent DESC
LIMIT 10;
-- Top produits
SELECT 
    product_id,
    SUM(sales) as total_sales
FROM sales_raw
GROUP BY product_id
ORDER BY total_sales DESC
LIMIT 10;
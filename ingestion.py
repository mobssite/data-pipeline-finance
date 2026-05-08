import pandas as pd
import sqlite3

# Load dataset
df = pd.read_csv("data/train.csv")

# Convert date column
df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True)

# Rename columns (important for clarity)
df = df.rename(columns={
    'Order Date': 'date',
    'Sales': 'sales',
    'Customer ID': 'customer_id',
    'Product ID': 'product_id'
})

# Drop missing values
df = df.dropna()

# Create database
conn = sqlite3.connect("finance.db")

# Save cleaned data
df.to_sql("sales_raw", conn, if_exists="replace", index=False)

print("Data loaded successfully")

cursor = conn.cursor()

query = """
SELECT 
    strftime('%Y-%m', date) AS month,
    SUM(sales) AS revenue
FROM sales_raw
GROUP BY month
ORDER BY month;
"""

cursor.execute(query)
result = cursor.fetchall()

print("\n📊 Revenue per month:\n")

for row in result:
    month, revenue = row
    print(f"{month} : {round(revenue, 2)}")

    query = """
SELECT 
    customer_id,
    SUM(sales) AS total_spent
FROM sales_raw
GROUP BY customer_id
ORDER BY total_spent DESC
LIMIT 10;
"""

cursor.execute(query)
result = cursor.fetchall()

print("\n👥 Top 10 Clients:\n")

for row in result:
    customer, revenue = row
    print(f"{customer} : {round(revenue, 2)}")

    query = """
SELECT 
    product_id,
    SUM(sales) AS total_sales
FROM sales_raw
GROUP BY product_id
ORDER BY total_sales DESC
LIMIT 10;
"""

cursor.execute(query)
result = cursor.fetchall()

print("\n📦 Top 10 Products:\n")

for row in result:
    product, revenue = row
    print(f"{product} : {round(revenue, 2)}")
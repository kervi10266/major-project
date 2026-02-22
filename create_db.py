import sqlite3
import random
from datetime import datetime, timedelta

conn = sqlite3.connect('sales.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS sales (
    order_id INTEGER PRIMARY KEY,
    product_name TEXT,
    category TEXT,
    price INTEGER,
    quantity INTEGER,
    total_amount INTEGER,
    order_date TEXT
)
''')

products = ["Laptop", "Phone", "Shoes", "Watch", "Headphones"]
categories = ["Electronics", "Fashion", "Fashion", "Accessories", "Electronics"]

for i in range(1, 1101):
    price = random.randint(500, 5000)
    quantity = random.randint(1, 5)
    total = price * quantity
    date = datetime.now() - timedelta(days=random.randint(0, 30))

    cursor.execute('''
    INSERT INTO sales (product_name, category, price, quantity, total_amount, order_date)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', (products[i % 5], categories[i % 5], price, quantity, total, date.strftime("%Y-%m-%d")))

conn.commit()
conn.close()

print("Database Created Successfully")
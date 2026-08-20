import datetime as dt
import random
import psycopg2

# Connect to your pipeline source database
conn = psycopg2.connect(
    dbname="pipeline_source",
    user="airbyte_user",
    password="admin",
    host="localhost",
)
cur = conn.cursor()

print("Setting up source tables...")
cur.execute(
    "DROP TABLE IF EXISTS order_items, orders, products, customers CASCADE;"
)

cur.execute("""
    CREATE TABLE customers (
        customer_id SERIAL PRIMARY KEY,
        name TEXT,
        email TEXT,
        signup_date DATE,
        country TEXT
    );
    CREATE TABLE products (
        product_id SERIAL PRIMARY KEY,
        name TEXT,
        category TEXT,
        unit_price NUMERIC(10,2)
    );
    CREATE TABLE orders (
        order_id SERIAL PRIMARY KEY,
        customer_id INT REFERENCES customers(customer_id),
        order_date TIMESTAMP,
        status TEXT
    );
    CREATE TABLE order_items (
        order_item_id SERIAL PRIMARY KEY,
        order_id INT REFERENCES orders(order_id),
        product_id INT REFERENCES products(product_id),
        quantity INT,
        line_total NUMERIC(10,2)
    );
""")
conn.commit()

countries = ["NG", "US", "UK", "IN", "BR", "DE", "ZA"]
categories = ["Phones", "Cases", "Chargers", "Cables", "Audio"]

print("Inserting mock customers...")
for i in range(1, 5001):
  cur.execute(
      "INSERT INTO customers (name, email, signup_date, country) VALUES (%s, %s, %s, %s)",
      (
          f"Customer {i}",
          f"c{i}@example.com",
          dt.date(2023, 1, 1) + dt.timedelta(days=random.randint(0, 800)),
          random.choice(countries),
      ),
  )

print("Inserting mock products...")
for i in range(1, 201):
  cur.execute(
      "INSERT INTO products (name, category, unit_price) VALUES (%s, %s, %s)",
      (
          f"Product {i}",
          random.choice(categories),
          round(random.uniform(5, 500), 2),
      ),
  )

print("Inserting mock orders and order items...")
for i in range(1, 50001):
  cust = random.randint(1, 5000)
  dt_ = dt.datetime(2024, 1, 1) + dt.timedelta(
      seconds=random.randint(0, 60 * 60 * 24 * 500)
  )

  # Insert order and fetch generated order_id
  cur.execute(
      "INSERT INTO orders (customer_id, order_date, status) VALUES (%s, %s, %s) RETURNING order_id",
      (
          cust,
          dt_,
          random.choice(["placed", "shipped", "delivered", "cancelled"]),
      ),
  )
  order_id = cur.fetchone()[0]

  # Insert 1 to 5 items per order
  for _ in range(random.randint(1, 5)):
    prod = random.randint(1, 200)
    qty = random.randint(1, 3)

    cur.execute(
        "SELECT unit_price FROM products WHERE product_id = %s", (prod,)
    )
    price = float(cur.fetchone()[0])

    cur.execute(
        "INSERT INTO order_items (order_id, product_id, quantity, line_total) VALUES (%s, %s, %s, %s)",
        (order_id, prod, qty, round(qty * price, 2)),
    )

conn.commit()
cur.close()
conn.close()
print("Source data loaded successfully.")
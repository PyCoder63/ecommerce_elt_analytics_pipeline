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

print("Fetching current max IDs (high-water marks) from source tables...")

# Helper function to get max ID safely
def get_max_id(table_name, id_column):
    cur.execute(f"SELECT COALESCE(MAX({id_column}), 0) FROM {table_name};")
    return cur.fetchone()[0]

max_customer_id = get_max_id("customers", "customer_id")
max_product_id = get_max_id("products", "product_id")
max_order_id = get_max_id("orders", "order_id")
max_order_item_id = get_max_id("order_items", "order_item_id")

print(f"Current Max IDs -> Customers: {max_customer_id}, Products: {max_product_id}, Orders: {max_order_id}, Order Items: {max_order_item_id}")

countries = ["NG", "US", "UK", "IN", "BR", "DE", "ZA"]
categories = ["Phones", "Cases", "Chargers", "Cables", "Audio"]

# 1. Insert new incremental customers
new_customers_count = 1000
print(f"Inserting {new_customers_count} new incremental customers...")
for i in range(1, new_customers_count + 1):
    next_id = max_customer_id + i
    cur.execute(
        "INSERT INTO customers (customer_id, name, email, signup_date, country) VALUES (%s, %s, %s, %s, %s)",
        (
            next_id,
            f"Customer {next_id}",
            f"c{next_id}@example.com",
            dt.date.today() - dt.timedelta(days=random.randint(0, 10)),
            random.choice(countries),
        ),
    )

# 2. Insert new incremental products
new_products_count = 20
print(f"Inserting {new_products_count} new incremental products...")
for i in range(1, new_products_count + 1):
    next_id = max_product_id + i
    cur.execute(
        "INSERT INTO products (product_id, name, category, unit_price) VALUES (%s, %s, %s, %s)",
        (
            next_id,
            f"Product {next_id}",
            random.choice(categories),
            round(random.uniform(10, 600), 2),
        ),
    )

# Refresh max customer ID references for foreign keys
latest_max_customer_id = max_customer_id + new_customers_count

# 3. Insert new incremental orders and order items
new_orders_count = 5000
print(f"Inserting {new_orders_count} new incremental orders and items...")
for i in range(1, new_orders_count + 1):
    # Reference customers dynamically (mix of old and newly inserted customers)
    cust = random.randint(1, latest_max_customer_id)
    dt_ = dt.datetime.now() - dt.timedelta(minutes=random.randint(0, 60 * 24 * 5))

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
        prod = random.randint(1, max_product_id + new_products_count)
        qty = random.randint(1, 3)

        cur.execute(
            "SELECT unit_price FROM products WHERE product_id = %s", (prod,)
        )
        price_result = cur.fetchone()
        price = float(price_result[0]) if price_result else 50.00

        cur.execute(
            "INSERT INTO order_items (order_id, product_id, quantity, line_total) VALUES (%s, %s, %s, %s)",
            (order_id, prod, qty, round(qty * price, 2)),
        )

conn.commit()
cur.close()
conn.close()
print("Incremental source data loaded successfully.")
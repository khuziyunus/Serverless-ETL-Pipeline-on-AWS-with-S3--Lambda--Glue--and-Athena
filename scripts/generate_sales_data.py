import csv
import random
import datetime

# Output file
filename = "raw_data/sample_sales_data.csv"

# Sample data
products = ['Laptop', 'Smartphone', 'Tablet', 'Monitor', 'Keyboard', 'Mouse', 'Headphones']
regions = ['North America', 'Europe', 'Asia', 'South America', 'Africa']
payment_methods = ['Credit Card', 'PayPal', 'Wire Transfer', 'Cash']

# Write header and rows
with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['order_id', 'product', 'price', 'quantity', 'total', 'region', 'payment_method', 'timestamp'])

    for i in range(1, 1001):
        product = random.choice(products)
        price = round(random.uniform(50, 1500), 2)
        quantity = random.randint(1, 5)
        total = round(price * quantity, 2)
        region = random.choice(regions)
        payment = random.choice(payment_methods)
        timestamp = datetime.datetime.now() - datetime.timedelta(days=random.randint(0, 365))

        writer.writerow([
            f"ORD{i:05d}",
            product,
            price,
            quantity,
            total,
            region,
            payment,
            timestamp.strftime("%Y-%m-%d %H:%M:%S")
        ])

print(f"✅ Sample dataset '{filename}' created with 1000 records.")

import sqlite3

# Connect to the restaurant database (creates a new one if it doesn't exist)
conn = sqlite3.connect('restaurant.db')

# Create a cursor object to execute SQL commands
cur = conn.cursor()

# Drop tables if they exist to start fresh each time
cur.execute('DROP TABLE IF EXISTS order_items')
cur.execute('DROP TABLE IF EXISTS invoices')
cur.execute('DROP TABLE IF EXISTS orders')
cur.execute('DROP TABLE IF EXISTS menu')
cur.execute('DROP TABLE IF EXISTS customers')  # Optional
cur.execute('DROP TABLE IF EXISTS staff')  # Optional

# Create table for menu
cur.execute('''CREATE TABLE IF NOT EXISTS menu (
                item_id INTEGER PRIMARY KEY,
                item_name TEXT NOT NULL,
                category TEXT NOT NULL,
                price REAL NOT NULL,
                description TEXT,
                available BOOLEAN NOT NULL
            )''')

# Create table for orders
cur.execute('''CREATE TABLE IF NOT EXISTS orders (
                order_id INTEGER PRIMARY KEY,
                customer_name TEXT NOT NULL,
                order_date DATETIME NOT NULL,
                status TEXT NOT NULL,
                total_amount REAL
            )''')

# Create table for order items
cur.execute('''CREATE TABLE IF NOT EXISTS order_items (
                order_item_id INTEGER PRIMARY KEY,
                order_id INTEGER,
                item_id INTEGER,
                quantity INTEGER NOT NULL,
                price REAL NOT NULL,
                FOREIGN KEY (order_id) REFERENCES orders (order_id),
                FOREIGN KEY (item_id) REFERENCES menu (item_id)
            )''')

# Create table for invoices/receipts
cur.execute('''CREATE TABLE IF NOT EXISTS invoices (
                invoice_id INTEGER PRIMARY KEY,
                order_id INTEGER,
                invoice_date DATETIME NOT NULL,
                payment_method TEXT NOT NULL,
                amount_paid REAL NOT NULL,
                FOREIGN KEY (order_id) REFERENCES orders (order_id)
            )''')

# Optional: Create table for customers (if you want to track them)
cur.execute('''CREATE TABLE IF NOT EXISTS customers (
                customer_id INTEGER PRIMARY KEY,
                customer_name TEXT NOT NULL,
                phone_number TEXT,
                email TEXT
            )''')

# Optional: Create table for staff (if you want to manage staff)
cur.execute('''CREATE TABLE IF NOT EXISTS staff (
                staff_id INTEGER PRIMARY KEY,
                staff_name TEXT NOT NULL,
                role TEXT NOT NULL,
                shift TEXT
            )''')

# Commit changes to create tables
conn.commit()

# Example of inserting data into the menu table
cur.execute('''INSERT INTO menu (item_name, category, price, description, available) 
               VALUES (?, ?, ?, ?, ?)''', 
               ('Cheeseburger', 'Main Course', 9.99, 'A juicy grilled cheeseburger', 1))
cur.execute('''INSERT INTO menu (item_name, category, price, description, available) 
               VALUES (?, ?, ?, ?, ?)''', 
               ('Fries', 'Appetizer', 3.99, 'Crispy golden fries', 1))

# Example of inserting an order
cur.execute('''INSERT INTO orders (customer_name, order_date, status, total_amount) 
               VALUES (?, ?, ?, ?)''', 
               ('John Doe', '2024-10-13 18:30:00', 'Completed', 13.98))

# Example of adding items to an order in the order_items table
cur.execute('''INSERT INTO order_items (order_id, item_id, quantity, price) 
               VALUES (?, ?, ?, ?)''', 
               (1, 1, 1, 9.99))  # Cheeseburger
cur.execute('''INSERT INTO order_items (order_id, item_id, quantity, price) 
               VALUES (?, ?, ?, ?)''', 
               (1, 2, 1, 3.99))  # Fries

# Example of adding an invoice for the order
cur.execute('''INSERT INTO invoices (order_id, invoice_date, payment_method, amount_paid) 
               VALUES (?, ?, ?, ?)''', 
               (1, '2024-10-13 18:35:00', 'Credit Card', 13.98))

# Commit changes to save data
conn.commit()

# Example query to fetch all menu items
cur.execute('''SELECT * FROM menu''')
menu_items = cur.fetchall()
print("\nMenu Items:")
print(f"{'Item ID':<10}{'Item Name':<20}{'Category':<15}{'Price':<10}{'Description':<30}{'Available'}")
for item in menu_items:
    print(f"{item[0]:<10}{item[1]:<20}{item[2]:<15}{item[3]:<10}{item[4]:<30}{item[5]}")

# Example query to fetch all orders
cur.execute('''SELECT * FROM orders''')
orders = cur.fetchall()
print("\nOrders:")
print(f"{'Order ID':<10}{'Customer Name':<20}{'Order Date':<25}{'Status':<15}{'Total Amount'}")
for order in orders:
    print(f"{order[0]:<10}{order[1]:<20}{order[2]:<25}{order[3]:<15}{order[4]}")

# Example query to fetch all order items for a specific order
cur.execute('''SELECT * FROM order_items WHERE order_id = ?''', (1,))
order_items = cur.fetchall()
print("\nOrder Items for Order 1:")
print(f"{'Order Item ID':<15}{'Order ID':<10}{'Item ID':<10}{'Quantity':<10}{'Price'}")
for order_item in order_items:
    print(f"{order_item[0]:<15}{order_item[1]:<10}{order_item[2]:<10}{order_item[3]:<10}{order_item[4]}")

# Close connection
conn.close()

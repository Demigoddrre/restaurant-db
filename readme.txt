Restaurant Database Project

Project Overview:
This project sets up a SQLite3 database to manage data for a restaurant, including menu items, 
customer orders, order details, and invoices. The goal is to create a structured relational database 
to simulate the operations of a restaurant, track orders, and manage menu items.

This project demonstrates the use of SQL commands for creating tables, inserting data, and running various 
queries to retrieve the necessary information. Additionally, it includes optional customer and staff tables to
extend functionality.

Database Schema:
The database is structured using the following tables:

Menu:
Stores information about each menu item offered by the restaurant.
Attributes:
item_id (Primary Key): Unique identifier for each menu item.
item_name: Name of the dish or beverage.
category: Category of the menu item (e.g., appetizer, main course, dessert).
price: The price of the menu item.
description: A brief description of the item.
available: A boolean value indicating whether the item is available.

Orders:
Contains information about customer orders, including customer name, the order date, status, and the 
total amount of the order.

Attributes:
order_id (Primary Key): Unique identifier for each order.
customer_name: Name of the customer placing the order.
order_date: Date and time the order was placed.
status: The status of the order (e.g., pending, completed).
total_amount: The total amount for the order.

Order Items:
This table links the orders and menu tables, storing information about the individual items in each order.

Attributes:
order_item_id (Primary Key): Unique identifier for each item in the order.
order_id (Foreign Key): Links to the orders table.
item_id (Foreign Key): Links to the menu table.
quantity: The quantity of the item ordered.
price: The price of the item at the time of the order.

Invoices/Receipts:
This table stores payment information for each order.

Attributes:
invoice_id (Primary Key): Unique identifier for each invoice.
order_id (Foreign Key): Links to the orders table.
invoice_date: Date when the invoice was generated.
payment_method: Payment method used by the customer (e.g., credit card, cash).
amount_paid: Total amount paid by the customer.

Customers (Optional):
Keeps track of customer information for loyalty programs or communications.

Attributes:
customer_id (Primary Key): Unique identifier for each customer.
customer_name: Name of the customer.
phone_number: Customer's phone number.
email: Customer's email address.

Staff (Optional):
Stores information about staff members at the restaurant.
Attributes:
staff_id (Primary Key): Unique identifier for each staff member.
staff_name: Name of the staff member.
role: The role of the staff member (e.g., waiter, chef).
shift: The shift of the staff member.
Functionality and SQL Queries:
Inserting Data into Tables:

Menu Items: Adds items to the menu table.
INSERT INTO menu (item_name, category, price, description, available) 
VALUES ('Cheeseburger', 'Main Course', 9.99, 'A juicy grilled cheeseburger', 1);


Orders: Adds customer orders to the orders table.
INSERT INTO orders (customer_name, order_date, status, total_amount) 
VALUES ('John Doe', '2024-10-13 18:30:00', 'Completed', 13.98);


Fetching Menu Items:
Retrieves all items in the menu table with a formatted output to show the item ID, name, category,
price, description, and availability.
SELECT * FROM menu;

Fetching Orders:
Retrieves all orders from the orders table, showing order ID, customer name, order date, status, and 
total amount.
SELECT * FROM orders;
Fetching Order Items:

Retrieves all items associated with a specific order (e.g., Order 1).
SELECT * FROM order_items WHERE order_id = 1;
Example Output:
Here’s an example of how the results are displayed:

Menu Items:

Item ID   Item Name           Category       Price     Description                   Available
1         Cheeseburger        Main Course    9.99      A juicy grilled cheeseburger   1
2         Fries               Appetizer      3.99      Crispy golden fries            1

Orders:
Order ID  Customer Name       Order Date               Status         Total Amount
1         John Doe            2024-10-13 18:30:00      Completed      13.98

Order Items for Order 1:
Order Item ID   Order ID  Item ID   Quantity   Price
1               1         1         1          9.99
2               1         2         1          3.99
Conclusion:
This SQLite3 project provides a functional simulation of restaurant operations, including managing a menu,
 placing orders, tracking the items ordered, and processing invoices. The schema is designed to cover the 
 essential features of a restaurant system, and the included queries provide easy access to the necessary 
 information for running a restaurant efficiently. The optional customer and staff tables offer flexibility
for extending the system further.
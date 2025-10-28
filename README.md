🏠 Home Inventory Tracking System

Crt Alt Elite — Database Implementation Project

📘 Overview

This project implements a Home Inventory Tracking System designed to help individuals record, organize, and manage information about their household possessions. It provides a structured and normalized database for tracking valuables, simplifying insurance claims, and maintaining an accurate record of assets.

The system includes:
	•	A MySQL database that defines all tables, relationships, and constraints.
	•	A Python program that connects to the database and allows users to execute predefined queries easily.

⸻

🎯 Objectives
	•	Design and implement a normalized relational database for home inventory management.
	•	Establish data integrity and enforce relationships between users, inventories, and items.
	•	Allow users to query and interact with the database using a simple Python interface.

⸻

🧩 Features
	•	Store and manage data for Users, Inventories, Items, Categories, Tags, Images, and Reports.
	•	Support one-to-many and many-to-many relationships using junction tables.
	•	Maintain referential integrity using foreign keys and cascading deletes.
	•	Provide SQL queries for simple, intermediate, and complex data retrieval operations.
	•	Include a Python interface for database interaction.

⸻

🏗️ Database Design

Entities
	•	User: Stores user credentials and account details.
	•	Inventory: Groups items belonging to a user.
	•	Item: Represents physical possessions with details like value, location, and condition.
	•	Category / Tag: Allows classification and flexible labeling of items.
	•	Image (Weak Entity): Stores photos linked to items.
	•	Report (Weak Entity): Stores generated summaries linked to inventories.

Relationships
	•	1:N:
	•	User → Inventory
	•	Inventory → Item
	•	Item → Image
	•	Inventory → Report
	•	M:N (Junction Tables):
	•	Item ↔ Category (Item_Category)
	•	Item ↔ Tag (Item_Tag)

The database is normalized to Third Normal Form (3NF) for consistency, minimal redundancy, and high data reliability.

⸻

⚙️ Setup & Usage

🧠 Requirements
	•	Python 3.x
	•	MySQL Server
	•	mysql-connector-python module

Install the connector:

pip install mysql-connector-python


⸻

🗄️ Database Setup
	1.	Open MySQL Workbench (or CLI).
	2.	Run the SQL file:

source path/to/inventory_system.sql;


	3.	Verify that all tables are created successfully:
	•	User
	•	Inventory
	•	Item
	•	Category
	•	Tag
	•	Item_Category
	•	Item_Tag
	•	Image
	•	Report

⸻

🐍 Python Script

The Python script (sqlConnection.py) allows interaction with the database.
It:
	•	Connects to MySQL using mysql.connector.
	•	Lets users select queries from a menu.
	•	Displays query results in a clean, readable format.
	•	Handles connection errors gracefully.

Example usage:

python sqlConnection.py


⸻

💻 Example SQL Queries

Type	Description	Example
Simple	List all users	SELECT user_id, username, email FROM User;
Intermediate	Count items per user	SELECT username, COUNT(item_id) FROM User JOIN Inventory USING(user_id) JOIN Item USING(inventory_id) GROUP BY username;
Complex	Show total inventory value per user	SELECT username, SUM(current_value) AS total_value FROM User JOIN Inventory USING(user_id) JOIN Item USING(inventory_id) GROUP BY username;


⸻

🧪 Testing & Validation

All components were tested in MySQL Workbench:
	•	✅ Database creation and foreign key validation
	•	✅ Data insertion without constraint violations
	•	✅ Query accuracy (10 test queries executed successfully)
	•	✅ Referential integrity with cascading deletes
	•	✅ Error handling and constraint enforcement

⸻

👥 Contributors

Name	Student No.	Contribution
Jean van Schalkwyk	4204301	SQL Querying, Testing & Validation
Kaamiel Isaacs	4129581	Database Design
Skye Jones (GL)	4122217	Database Implementation, Normalization & Conclusion
Thaakirah Mosoval	4314422	Business Rules & Introduction
Uwais Cornelius	4121659	Python Integration & GitHub Repository


⸻

📚 References
	•	Coronel, C., & Morris, S. Database Systems: Design, Implementation, & Management (13th Ed.)
	•	GeeksforGeeks: Database Design in DBMS
	•	DataCamp: SQL Normalization Tutorial

⸻

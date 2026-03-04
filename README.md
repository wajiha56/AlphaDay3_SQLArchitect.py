# 🏗️ AlphaDay3_SQLArchitect

Engineered a local SQLite database to query high-earning employee brackets.  
This project demonstrates the journey from flat CSV data to a structured, relational architecture using Python and SQLite, giving you the skills to query high-value insights efficiently.

To get started, clone the repository and navigate into it:

git clone https://github.com/yourusername/AlphaDay3_SQLArchitect.git  
cd AlphaDay3_SQLArchitect


Below is the Python script that creates the database, inserts sample data, and queries high-earning employees:

import sqlite3

# Connect to SQLite database (creates file if it doesn't exist)
conn = sqlite3.connect("Alpha_Company.db")
cursor = conn.cursor()

# Create Employee table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Employee (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    department TEXT,
    salary REAL
)
""")

# Insert sample data (ignore if already inserted)
cursor.executemany("""
INSERT INTO Employee (name, department, salary)
VALUES (?, ?, ?)
""", [
    ("Alice", "Engineering", 95000),
    ("Bob", "Marketing", 60000),
    ("Charlie", "Engineering", 120000),
    ("Diana", "HR", 70000)
])

conn.commit()

# Query high-earning employees (salary > 90000)
cursor.execute("SELECT * FROM Employee WHERE salary > 90000")
results = cursor.fetchall()

print("High-Earning Employees:")
for row in results:
    print(row)

conn.close()

# To run the script, use the following command:

python AlphaDay3_SQLArchitect.py

# Expected output:

High-Earning Employees:
(1, 'Alice', 'Engineering', 95000.0)
(3, 'Charlie', 'Engineering', 120000.0)

# Key Features:
- Relational database design with SQLite
- High-earning employee query using SQL
- Structured Python script for automated querying
- Ready for GitHub deployment and collaborative work

# Learning Takeaways:
- Transition from flat data files to relational architecture
- Apply declarative SQL logic for data management
- Execute queries to extract instant business insights
- Achieve the level of Junior Database Architect

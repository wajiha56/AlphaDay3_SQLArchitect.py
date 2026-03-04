# 🏗️ AlphaDay3_SQLArchitect

**Engineered a local SQLite database to query high-earning employee brackets.**  

This project demonstrates the journey from flat CSV data to a structured, relational architecture using Python and SQLite, giving you the skills to query high-value insights efficiently.

---

## 📂 Project Contents

- **Database:** `Alpha_Company.db`  
- **Python Script:** `AlphaDay3_SQLArchitect.py`  
- **Purpose:** Learn database generation, SQL declarative logic, and query execution.  

---

## 🚀 Objectives

By the end of this project, you will have mastered:

1. **Database Generation**  
   - Move beyond flat CSV files into structured, relational tables.  
   - Design tables for employees, departments, and salaries.  

2. **Declarative Logic**  
   - Learn SQL, the universal language for data management used by Amazon, Meta, Google, and others.  

3. **Query Execution**  
   - Pull specific, high-value insights from raw tables instantly.  
   - Example: Identify employees earning above a certain salary threshold.

---

## 💻 How to Run & Script

This section contains everything you need to **run the project** and **understand the Python script**.
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

### 3️⃣ Run the script
python AlphaDay3_SQLArchitect.py

### Expected Output
High-Earning Employees:
(1, 'Alice', 'Engineering', 95000.0)
(3, 'Charlie', 'Engineering', 120000.0)

## 📊 Key Features

- Relational database design with SQLite  
- High-earning employee query using SQL  
- Structured Python script for automated querying  
- Ready for GitHub deployment and collaborative work

  ## 💡 Learning Takeaways

- Transition from flat data files to **relational architecture**  
- Apply **declarative SQL logic** for data management  
- Execute queries to extract **instant business insights**  
- Achieve the level of **Junior Database Architect**

### 1️⃣ Clone the repository

```bash
git clone https://github.com/yourusername/AlphaDay3_SQLArchitect.git
cd AlphaDay3_SQLArchitect



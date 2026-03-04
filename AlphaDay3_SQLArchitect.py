import sqlite3
import pandas as pd


# 1️⃣ Create Database Connection (creates file automatically)
conn = sqlite3.connect("Alpha_Company.db")
cursor = conn.cursor()


# 2️⃣ Create Staff Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Staff (
    Employee_ID INTEGER PRIMARY KEY,
    Name TEXT,
    Department TEXT,
    Salary INTEGER
)
""")


# 3️⃣ Insert Staff Data
staff_data = [
    (1, "Ali", "IT", 120000),
    (2, "Sara", "Marketing", 85000),
    (3, "Ahmed", "IT", 150000),
    (4, "Fatima", "Sales", 95000),
    (5, "Zain", "IT", 75000),
]

cursor.executemany(
    "INSERT OR IGNORE INTO Staff VALUES (?, ?, ?, ?)",
    staff_data,
)

conn.commit()


# 4️⃣ Query: IT staff earning above 100000
print("---- High Earners in IT ----")

query = """
SELECT Name, Salary
FROM Staff
WHERE Department = 'IT' AND Salary > 100000
"""

result_df = pd.read_sql_query(query, conn)
print(result_df)


# 5️⃣ Close Connection
conn.close()

print("\nDatabase created successfully!")
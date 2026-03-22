# ================================================================
#  Expense Tracker — Demo Database Generator
#  Run this file ONCE to create expenses.db with sample data.
#  Author : Aditya Bobade
# ================================================================

import sqlite3

# ----------------------------------------------------------------
# Connect / Create database
# ----------------------------------------------------------------

conn = sqlite3.connect("expenses.db")
cursor = conn.cursor()

# ----------------------------------------------------------------
# Create table
# ----------------------------------------------------------------

cursor.execute("""
    CREATE TABLE IF NOT EXISTS expenses (
        id          INTEGER PRIMARY KEY AUTOINCREMENT,
        description TEXT    NOT NULL,
        category    TEXT    NOT NULL,
        amount      REAL    NOT NULL,
        date        TEXT    NOT NULL
    )
""")

# ----------------------------------------------------------------
# Insert demo data
# ----------------------------------------------------------------

demo_expenses = [
    ("Lunch at Cafe",           "Food",     250.00,  "2025-01-05"),
    ("Metro Card Recharge",     "Travel",   500.00,  "2025-01-07"),
    ("Electricity Bill",        "Bills",    1200.00, "2025-01-10"),
    ("Amazon Order - Books",    "Shopping", 899.00,  "2025-01-12"),
    ("Dinner with Friends",     "Food",     750.00,  "2025-01-15"),
    ("Uber Ride",               "Travel",   180.00,  "2025-01-17"),
    ("Netflix Subscription",    "Bills",    649.00,  "2025-01-20"),
    ("Grocery Shopping",        "Food",     1350.00, "2025-01-22"),
    ("New Headphones",          "Shopping", 2499.00, "2025-01-25"),
    ("Bus Pass Monthly",        "Travel",   400.00,  "2025-01-28"),
    ("Internet Bill",           "Bills",    799.00,  "2025-02-01"),
    ("Breakfast - Canteen",     "Food",     120.00,  "2025-02-03"),
    ("Shoes Purchase",          "Shopping", 1799.00, "2025-02-06"),
    ("Petrol",                  "Travel",   600.00,  "2025-02-08"),
    ("Mobile Recharge",         "Bills",    299.00,  "2025-02-10"),
    ("Pizza Night",             "Food",     480.00,  "2025-02-13"),
    ("Flight Ticket",           "Travel",   4500.00, "2025-02-15"),
    ("Stationery",              "Other",    150.00,  "2025-02-17"),
    ("Gym Membership",          "Other",    1000.00, "2025-02-20"),
    ("Birthday Gift",           "Shopping", 999.00,  "2025-02-22"),
]

cursor.executemany(
    "INSERT INTO expenses (description, category, amount, date) VALUES (?, ?, ?, ?)",
    demo_expenses
)

conn.commit()

# ----------------------------------------------------------------
# Confirm
# ----------------------------------------------------------------

count = cursor.execute("SELECT COUNT(*) FROM expenses").fetchone()[0]
total = cursor.execute("SELECT SUM(amount) FROM expenses").fetchone()[0]

conn.close()

print(f"✅ expenses.db created successfully!")
print(f"   Records inserted : {count}")
print(f"   Total amount     : ₹ {total:,.2f}")

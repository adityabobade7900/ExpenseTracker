# ================================================================
#  Expense Tracker — Flask Backend
#  Author : Aditya Bobade
# ================================================================

from flask import Flask, render_template, request, redirect, url_for, jsonify
import sqlite3

app = Flask(__name__)

# ----------------------------------------------------------------
# DATABASE CONNECTION
# ----------------------------------------------------------------

def get_db_connection():
    """Open and return a SQLite connection with Row factory enabled."""
    conn = sqlite3.connect("expenses.db")
    conn.row_factory = sqlite3.Row
    return conn


# ----------------------------------------------------------------
# DATABASE INITIALISATION — runs once on startup
# ----------------------------------------------------------------

def init_db():
    """Create the expenses table if it does not already exist."""
    conn = get_db_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            description TEXT    NOT NULL,
            category    TEXT    NOT NULL,
            amount      REAL    NOT NULL,
            date        TEXT    NOT NULL
        )
    """)
    conn.commit()
    conn.close()


init_db()


# ----------------------------------------------------------------
# HOME PAGE  —  GET /
# ----------------------------------------------------------------

@app.route("/")
def index():
    """Fetch all expenses ordered by date and compute the total."""
    conn = get_db_connection()

    expenses = conn.execute(
        "SELECT * FROM expenses ORDER BY date DESC"
    ).fetchall()

    total = conn.execute(
        "SELECT COALESCE(SUM(amount), 0) FROM expenses"
    ).fetchone()[0]

    conn.close()
    return render_template("index.html", expenses=expenses, total=round(total, 2))


# ----------------------------------------------------------------
# ADD EXPENSE  —  POST /add
# ----------------------------------------------------------------

@app.route("/add", methods=["POST"])
def add_expense():
    """Insert a new expense record into the database."""
    description = request.form["description"].strip()
    category    = request.form["category"].strip()
    amount      = request.form["amount"].strip()
    date        = request.form["date"].strip()

    # Basic server-side validation
    if not description or not category or not amount or not date:
        return redirect(url_for("index"))

    try:
        amount = float(amount)
        if amount <= 0:
            return redirect(url_for("index"))
    except ValueError:
        return redirect(url_for("index"))

    conn = get_db_connection()
    conn.execute(
        "INSERT INTO expenses (description, category, amount, date) VALUES (?, ?, ?, ?)",
        (description, category, amount, date)
    )
    conn.commit()
    conn.close()

    return redirect(url_for("index"))


# ----------------------------------------------------------------
# EDIT PAGE  —  GET /edit/<id>
# FIX: this route was missing — edit.html had no page to load it
# ----------------------------------------------------------------

@app.route("/edit/<int:id>")
def edit_expense(id):
    """Load the edit form pre-filled with the selected expense."""
    conn = get_db_connection()
    expense = conn.execute(
        "SELECT * FROM expenses WHERE id = ?", (id,)
    ).fetchone()
    conn.close()

    if expense is None:
        return redirect(url_for("index"))

    return render_template("edit.html", expense=expense)


# ----------------------------------------------------------------
# UPDATE EXPENSE  —  POST /update/<id>
# FIX: this route was completely missing from the original app
# ----------------------------------------------------------------

@app.route("/update/<int:id>", methods=["POST"])
def update_expense(id):
    """Update an existing expense record."""
    description = request.form["description"].strip()
    category    = request.form["category"].strip()
    amount      = request.form["amount"].strip()
    date        = request.form["date"].strip()

    try:
        amount = float(amount)
        if amount <= 0:
            return redirect(url_for("edit_expense", id=id))
    except ValueError:
        return redirect(url_for("edit_expense", id=id))

    conn = get_db_connection()
    conn.execute(
        """UPDATE expenses
           SET description = ?, category = ?, amount = ?, date = ?
           WHERE id = ?""",
        (description, category, amount, date, id)
    )
    conn.commit()
    conn.close()

    return redirect(url_for("index"))


# ----------------------------------------------------------------
# DELETE EXPENSE  —  POST /delete/<id>
# FIX: changed from GET to POST — deleting via GET is unsafe
# ----------------------------------------------------------------

@app.route("/delete/<int:id>", methods=["POST"])
def delete_expense(id):
    """Delete an expense record by ID."""
    conn = get_db_connection()
    conn.execute("DELETE FROM expenses WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for("index"))


# ----------------------------------------------------------------
# CHART DATA  —  GET /chart-data
# ----------------------------------------------------------------

@app.route("/chart-data")
def chart_data():
    """Return category-wise expense totals as JSON for Chart.js."""
    conn = get_db_connection()
    rows = conn.execute("""
        SELECT category, ROUND(SUM(amount), 2) AS total
        FROM expenses
        GROUP BY category
        ORDER BY total DESC
    """).fetchall()
    conn.close()

    labels = [row["category"] for row in rows]
    values = [row["total"]    for row in rows]

    return jsonify({"labels": labels, "values": values})


# ----------------------------------------------------------------
# RUN
# ----------------------------------------------------------------

if __name__ == "__main__":
    app.run(debug=True)

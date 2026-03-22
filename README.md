# 💰 Expense Tracker

> **Author:** Aditya Bobade &nbsp;|&nbsp; **Language:** Python 3.8+ &nbsp;|&nbsp; **Framework:** Flask &nbsp;|&nbsp; **License:** Educational Use Only

---

## 📋 Table of Contents

1. [Project Overview](#-project-overview)
2. [Features](#-features)
3. [Technologies Used](#-technologies-used)
4. [Database Design](#-database-design)
5. [Project Structure](#-project-structure)
6. [Prerequisites](#-prerequisites)
7. [Installation & Setup](#-installation--setup)
8. [Running the Application](#-running-the-application)
9. [Usage Guide](#-usage-guide)
10. [API Routes](#-api-routes)
11. [Known Notes & Tips](#-known-notes--tips)
12. [Contributing](#-contributing)
13. [Need Help?](#-need-help)
14. [License](#-license)

---

## 📌 Project Overview

The **Expense Tracker** is a lightweight web application built with **Python (Flask)** and **SQLite**. It allows users to record, view, edit, and delete daily expenses through a clean and responsive web interface. All data is stored locally in a SQLite database file — no external database server required.

The application also includes an interactive **Chart.js** powered chart that visualises spending by category, with support for multiple chart types (Bar, Pie, Doughnut, Polar Area, Line).

---

## ✅ Features

- **Add** new expense records with description, category, amount, and date
- **View** all expenses in a clean table sorted by date (newest first)
- **Edit** any existing expense via a pre-filled form
- **Delete** any expense with a confirmation prompt
- **Total** expense summary displayed on the main page
- **Category badges** — colour-coded labels for each category
- **Interactive chart** — visualise spending by category with 5 chart type options
- **Responsive design** — works on desktop and mobile screens
- **Empty state** — friendly message when no expenses are recorded
- **Demo database** — sample data script included for quick testing

---

## 🛠️ Technologies Used

| Component      | Technology           | Purpose                                          |
|----------------|----------------------|--------------------------------------------------|
| Language       | Python 3.8+          | Backend logic                                    |
| Web Framework  | Flask                | Routing, templating, request handling            |
| Database       | SQLite               | Local persistent storage — no server needed      |
| Templating     | Jinja2               | Dynamic HTML rendering (built into Flask)        |
| Frontend       | HTML5 + CSS3         | Structure and styling                            |
| Charts         | Chart.js (CDN)       | Interactive expense breakdown charts             |
| Font           | Segoe UI / Arial     | Clean readable typography                        |

---

## 🗄️ Database Design

**Database file:** `expenses.db` (SQLite — auto-created on first run)

**Table name:** `expenses`

| Column        | Data Type | Constraint                 | Description                                       |
|---------------|-----------|----------------------------|---------------------------------------------------|
| `id`          | INTEGER   | PRIMARY KEY, AUTOINCREMENT | Unique record ID — set automatically              |
| `description` | TEXT      | NOT NULL                   | Short description of the expense                  |
| `category`    | TEXT      | NOT NULL                   | One of: Food, Travel, Shopping, Bills, Other      |
| `amount`      | REAL      | NOT NULL                   | Expense amount in ₹ (supports decimals)           |
| `date`        | TEXT      | NOT NULL                   | Date in `YYYY-MM-DD` format                       |

> **Note:** The database and table are created automatically when you run `app.py` for the first time via the `init_db()` function. You do not need to set anything up manually.

---

## 📁 Project Structure

```
ExpenseTracker/
│
├── app.py                →  Flask backend — all routes and database logic
├── create_demo_db.py     →  One-time script — creates expenses.db with 20 sample records
├── .gitignore            →  Excludes database, cache, venv from GitHub
├── README.md             →  Project documentation (this file)
│
├── static/
│   └── style.css         →  All CSS styling — layout, buttons, badges, chart, responsive
│
└── templates/
    ├── index.html        →  Main page — add form, expenses table, chart
    └── edit.html         →  Edit page — pre-filled update form for a single expense
```

---

## 📦 Prerequisites

Make sure the following are installed on your system:

| Requirement | Version      | Download Link                             |
|-------------|--------------|-------------------------------------------|
| Python      | 3.8 or above | https://www.python.org/downloads/         |
| pip         | Latest       | Comes bundled with Python                 |
| Flask       | Latest       | Install via pip (see Step 2 below)        |

> **Note:** SQLite comes built into Python — no separate installation needed.

---

## ⚙️ Installation & Setup

### Step 1 — Download or clone the project

**Option A — Clone from GitHub:**
```powershell
git clone https://github.com/adityabobade7900/ExpenseTracker.git
cd ExpenseTracker
```

**Option B — Download ZIP:**
Download and extract the ZIP from GitHub, then navigate into the folder:
```powershell
cd "C:\Users\bobad\Downloads\ExpenseTracker"
```

---

### Step 2 — Install Flask
```powershell
pip install flask
```

---

### Step 3 — (Optional) Create demo data
If you want to start with sample expense records instead of an empty database, run:
```powershell
python create_demo_db.py
```

You should see:
```
✅ expenses.db created successfully!
   Records inserted : 20
   Total amount     : ₹ 21,123.00
```

This inserts 20 sample expenses across all 5 categories.
If you skip this step, `app.py` will create a fresh empty database automatically on first run.

---

## ▶️ Running the Application

```powershell
python app.py
```

You should see:
```
 * Running on http://127.0.0.1:5000
 * Debug mode: on
```

Open your browser and go to:
```
http://127.0.0.1:5000
```

To stop the server press `Ctrl + C` in PowerShell.

---

## 📖 Usage Guide

### Main Page (`/`)

#### ➕ Adding an Expense
1. Fill in the **Description** field (e.g. "Lunch at cafe")
2. Select a **Category** from the dropdown (Food, Travel, Shopping, Bills, Other)
3. Enter the **Amount** in ₹ (decimals supported, e.g. `149.50`)
4. Pick a **Date** using the date picker
5. Click **+ Add Expense**
6. The page refreshes and the new record appears at the top of the table

#### 👁️ Viewing Expenses
- All expenses are listed in the table sorted by **date descending** (newest first)
- Each category shows a **coloured badge** for quick identification
- The **Total Expenses** card at the top shows the running sum of all records

#### ✏️ Editing an Expense
1. Click the **Edit** button (blue) on any row
2. You are taken to the Edit page with all fields pre-filled
3. Modify any field you want
4. Click **💾 Save Changes** to update the record
5. Click **✕ Cancel** to go back without saving

#### 🗑️ Deleting an Expense
1. Click the **Delete** button (red) on any row
2. A confirmation dialog appears — click **OK** to confirm or **Cancel** to abort
3. The record is permanently removed from the database

#### 🧹 Empty State
If no expenses are recorded, the table area shows:
```
No expenses recorded yet. Add your first one above!
```

---

### Chart Section

The **Expense Breakdown** chart at the bottom of the main page shows spending grouped by category.

| Chart Type  | Best For                               |
|-------------|----------------------------------------|
| Bar         | Comparing amounts across categories    |
| Pie         | Seeing proportion of each category     |
| Doughnut    | Same as pie with a cleaner look        |
| Polar Area  | Comparing with size and angle          |
| Line        | Trend-style view of category spending  |

Use the **Chart Type** dropdown to switch between chart styles instantly.

---

## 🔗 API Routes

| Method | Route           | Description                                       |
|--------|-----------------|---------------------------------------------------|
| GET    | `/`             | Home page — loads all expenses and total          |
| POST   | `/add`          | Add a new expense from the form                   |
| GET    | `/edit/<id>`    | Load edit page pre-filled with expense data       |
| POST   | `/update/<id>`  | Save updated expense data to the database         |
| POST   | `/delete/<id>`  | Delete an expense by ID                           |
| GET    | `/chart-data`   | Returns JSON of category totals for Chart.js      |

---

## 💡 Known Notes & Tips

- **Database location** — `expenses.db` is created in the same folder as `app.py`. Do not move it while the app is running.

- **Delete uses POST** — The delete action uses a `<form method="post">` instead of a plain `<a href>` link. This is intentional — deleting data via a GET request is unsafe because browsers and bots can trigger GET links accidentally.

- **Server-side validation** — `app.py` validates all fields on the server before inserting or updating. Empty fields and negative or zero amounts are rejected even if someone bypasses the browser form.

- **Chart data is live** — The chart fetches data from `/chart-data` every time the page loads or the chart type is changed. It always reflects the current state of the database.

- **Debug mode** — The app runs with `debug=True` by default. This is fine for local development but should be turned off before deploying to a live server:
  ```python
  app.run(debug=False)
  ```

- **expenses.db is in .gitignore** — The database file is excluded from GitHub intentionally. It contains personal data and is auto-recreated on every fresh setup.

---

## 🤝 Contributing

Contributions are welcome for learning and improvement purposes.

1. Fork this repository
2. Create a new feature branch:
```powershell
git checkout -b feature/your-feature-name
```
3. Make your changes and commit:
```powershell
git commit -m "Add: description of what you changed"
```
4. Push your branch:
```powershell
git push origin feature/your-feature-name
```
5. Open a **Pull Request** and describe what you changed and why

---

## 📞 Need Help?

If you have any questions, suggestions, or run into any issues, feel free to reach out:

| Platform    | Link                                                                          |
|-------------|-------------------------------------------------------------------------------|
| 💼 LinkedIn  | [linkedin.com/in/adityabobade](https://linkedin.com/in/adityabobade)          |
| 📧 Email     | [bobade1436@gmail.com](mailto:bobade1436@gmail.com)                           |

---

## 📜 License

```
Copyright © 2025 Aditya Bobade

This project is intended for EDUCATIONAL PURPOSES ONLY.
You may use, modify, and share this project for learning or personal research.
Commercial use, selling, or redistribution for profit is strictly NOT permitted.
All rights reserved.
```

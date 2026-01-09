from flask import Flask, render_template, request, redirect, session
import sqlite3
from datetime import datetime

app = Flask(__name__)
app.secret_key = "tasksync_secret"

DB_NAME = "database.db"

def get_db():
    return sqlite3.connect(DB_NAME)

# ---------- DATABASE SETUP ----------
conn = get_db()
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY,
    password TEXT
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    description TEXT,
    created_at TEXT,
    username TEXT
)
""")

conn.commit()
conn.close()

# ---------- LOGIN ----------
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        conn = get_db()
        cur = conn.cursor()
        cur.execute(
            "SELECT * FROM users WHERE username=? AND password=?",
            (request.form["username"], request.form["password"])
        )
        user = cur.fetchone()
        conn.close()

        if user:
            session["user"] = request.form["username"]
            return redirect("/dashboard")

    return render_template("login.html")

# ---------- REGISTER ----------
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        conn = get_db()
        cur = conn.cursor()
        try:
            cur.execute(
                "INSERT INTO users VALUES (?, ?)",
                (request.form["username"], request.form["password"])
            )
            conn.commit()
        except:
            pass
        conn.close()
        return redirect("/")

    return render_template("register.html")

# ---------- DASHBOARD ----------
@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect("/")

    conn = get_db()
    cur = conn.cursor()
    cur.execute(
        """
        SELECT id, title, description, created_at
        FROM tasks
        WHERE username=?
        ORDER BY id DESC
        """,
        (session["user"],)
    )
    tasks = cur.fetchall()
    conn.close()

    return render_template("dashboard.html", tasks=tasks)

# ---------- ADD TASK ----------
@app.route("/add", methods=["POST"])
def add_task():
    if "user" not in session:
        return redirect("/")

    title = request.form["title"]
    description = request.form.get("description", "")
    created_at = datetime.now().strftime("%d %b %Y, %I:%M %p")

    conn = get_db()
    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO tasks (title, description, created_at, username)
        VALUES (?, ?, ?, ?)
        """,
        (title, description, created_at, session["user"])
    )
    conn.commit()
    conn.close()

    return redirect("/dashboard")

# ---------- EDIT TASK ----------
@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_task(id):
    if "user" not in session:
        return redirect("/")

    conn = get_db()
    cur = conn.cursor()

    if request.method == "POST":
        cur.execute(
            """
            UPDATE tasks
            SET title=?, description=?
            WHERE id=?
            """,
            (request.form["title"], request.form["description"], id)
        )
        conn.commit()
        conn.close()
        return redirect("/dashboard")

    cur.execute(
        "SELECT title, description FROM tasks WHERE id=?",
        (id,)
    )
    task = cur.fetchone()
    conn.close()

    return render_template("edit.html", task=task)

# ---------- DELETE ----------
@app.route("/delete/<int:id>")
def delete_task(id):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("DELETE FROM tasks WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return redirect("/dashboard")

# ---------- LOGOUT ----------
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)

# Input Library

from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
import re
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Secret key for secure session handling
app.secret_key = "Atri_SecureLogin_20026_9xK"

DATABASE = "database.db"


# -------------------------
# Database Connection
# -------------------------
def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


# -------------------------
# Create Database
# -------------------------
def create_database():

    conn = get_db()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


# -------------------------
# Input Validation
# -------------------------
def valid_email(email):

    pattern = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"

    return re.match(pattern, email) is not None

def strong_password(password):
    if len(password) < 8:
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"[0-9]", password):
        return False
    return True

# -------------------------
# Home
# -------------------------
@app.route("/")
def home():

    if "user_id" in session:
        return redirect(url_for("dashboard"))

    return redirect(url_for("login"))

# -------------------------
# Registration
# -------------------------
@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")

        # Input validation
        if not name:
            return "Name is required."

        if not valid_email(email):
            return "Invalid email address."

        if not strong_password(password):
            return (
                "Password must contain at least 8 characters, "
                "one uppercase letter, one lowercase letter and one number."
            )

        # Password hashing
        hashed_password = generate_password_hash(password)

        try:

            conn = get_db()

            conn.execute(
                """
                INSERT INTO users (name, email, password)
                VALUES (?, ?, ?)
                """,
                (name, email, hashed_password)
            )

            conn.commit()
            conn.close()

            return redirect(url_for("login"))

        except sqlite3.IntegrityError:

            return "Email already registered."

    return render_template("register.html")


# -------------------------
# Login / Authentication
# -------------------------
@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")

        conn = get_db()

        user = conn.execute(
            "SELECT * FROM users WHERE email = ?",
            (email,)
        ).fetchone()

        conn.close()

        # Verify password hash
        if user and check_password_hash(user["password"], password):

            # Session handling
            session.clear()

            session["user_id"] = user["id"]
            session["user_name"] = user["name"]

            return redirect(url_for("dashboard"))

        return "Invalid email or password."

    return render_template("login.html")


# -------------------------
# Protected Dashboard
# -------------------------
@app.route("/dashboard")
def dashboard():

    # Authentication check
    if "user_id" not in session:
        return redirect(url_for("login"))

    return render_template(
        "dashboard.html",
        name=session["user_name"]
    )

# -------------------------
# Logout
# -------------------------
@app.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("login"))

# -------------------------
# Start Application
# -------------------------
if __name__ == "__main__":

    create_database()

    app.run(debug=True)
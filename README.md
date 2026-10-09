# 🔐 Implementation of Secure Coding Practices

A Python Flask web application demonstrating essential secure coding practices, including input validation, password hashing, session handling, authentication, and authorization.

## 📌 Project Overview

This project implements a secure user registration and login system using Flask and SQLite. It demonstrates how common security practices can help protect user accounts, validate input, and restrict access to protected resources.

The application allows users to register, log in, access a protected dashboard, and log out securely.

## 🎯 Objectives

* Implement input validation for user registration.
* Store passwords securely using password hashing.
* Manage authenticated user sessions.
* Implement user authentication and protected routes.
* Demonstrate basic authorization checks.
* Test the application against common input and authentication errors.

## 🛠️ Technologies Used

* **Python** – Backend programming
* **Flask** – Web application framework
* **SQLite** – Database management
* **HTML** – Frontend forms and pages
* **Werkzeug Security** – Password hashing and verification
* **Regular Expressions** – Input validation

## ✨ Features

### 1. Input Validation

* Validates email format.
* Checks that required fields are provided.
* Enforces minimum password length and character requirements.
* Prevents duplicate email registration through a database constraint.

### 2. Password Hashing

* Uses Werkzeug's `generate_password_hash()` to hash passwords.
* Uses `check_password_hash()` to verify passwords during login.
* Avoids storing passwords in plain text.

### 3. Session Handling

* Maintains login state using Flask sessions.
* Stores the authenticated user's ID and name in the session.
* Clears session data during logout.

### 4. Authentication

* Verifies user credentials against stored account information.
* Displays a generic error message when login fails.
* Redirects authenticated users to their dashboard.

### 5. Protected Routes

* Restricts dashboard access to authenticated users.
* Redirects unauthenticated users to the login page.

## 📂 Project Structure

```text
SecureCoding_Project/
│
├── app.py
├── database.db
├── README.md
│
└── templates/
    ├── register.html
    ├── login.html
    └── dashboard.html
```

**Note:** `database.db` is generated automatically when the database initialization function runs. Do not commit a database containing real user information.

## ⚙️ Installation and Setup

### Prerequisites

* Python 3.10 or later
* pip
* Git (optional)

### Step 1: Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
```

Replace the URL with your actual GitHub repository URL.

### Step 2: Open the Project Directory

```bash
cd SecureCoding_Project
```

### Step 3: Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

### Step 4: Install Dependencies

```bash
python -m pip install Flask
```

### Step 5: Configure the Secret Key

If your application reads its secret key from the `SECRET_KEY` environment variable, set a development key in PowerShell:

```powershell
$env:SECRET_KEY = "replace-with-a-random-secret"
```

Use a strong, private secret key. Never commit it to GitHub.

### Step 6: Run the Application

```bash
python app.py
```

Open your browser and visit:

* Registration: `http://127.0.0.1:5000/register`
* Login: `http://127.0.0.1:5000/login`
* Dashboard: `http://127.0.0.1:5000/dashboard`

## 🧪 Security Testing

Test the application using the following scenarios:

| Test Case                      | Expected Result                    |
| ------------------------------ | ---------------------------------- |
| Valid registration             | Account is created                 |
| Invalid email                  | Registration is rejected           |
| Weak password                  | Registration is rejected           |
| Duplicate email                | Duplicate account is rejected      |
| Correct credentials            | Login succeeds                     |
| Incorrect password             | Login fails                        |
| Access dashboard without login | Redirects to login                 |
| Logout                         | Session is cleared                 |
| Inspect stored password        | Password is hashed, not plain text |

Record the actual results after executing each test.

## 🔒 Security Considerations

This project demonstrates foundational secure coding practices. Before production deployment, consider implementing:

* CSRF protection for forms.
* Login rate limiting and brute-force protection.
* Secure session-cookie settings.
* Environment-based secret-key management.
* Role-based access control where required.
* HTTPS and production-safe server configuration.
* Appropriate error handling and security logging.

**Important:** Flask's development server and debug mode are intended for local development, not production deployment.

## 🎓 Learning Outcomes

By completing this project, learners can understand:

* Secure input validation.
* Password hashing and verification.
* Authentication and session management.
* Protected routes and authorization checks.
* Basic security testing and documentation.

## 🚀 Future Improvements

* Add an administrator role with role-based permissions.
* Add CSRF protection and login rate limiting.
* Improve the user interface with CSS and responsive design.
* Add automated tests using `pytest`.
* Add password reset and account management features.

## 👨‍💻 Author
**Atri Koley**

Cybersecurity Project – Secure Coding Practices

## 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for details.


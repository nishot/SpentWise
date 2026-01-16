# 💰 SpentWise – Personal Finance API

**SpentWise** is a robust backend REST API built with **FastAPI** and **PostgreSQL**.
It allows users to track daily expenses, categorize spending, and manage personal finances securely.

The system is built with **security-first principles**, using **JWT authentication** and **password hashing** to ensure data privacy and ownership protection.

---

## 🚀 Features

* 🔐 **User Authentication**
  Secure registration and login using OAuth2 with JWT tokens.

* 💸 **Expense Tracking**
  Full CRUD operations for managing personal expenses.

* 🗂 **Relational Data Modeling**
  Expenses are linked to specific **Users** and **Categories** via foreign keys.

* 🔒 **Ownership Protection**
  Users can only view, update, or delete their own data.

* 📑 **Automatic Documentation**
  Interactive API documentation provided by Swagger UI.

---

## 🛠 Tech Stack

* **Framework**: FastAPI
* **Database**: PostgreSQL
* **ORM**: SQLAlchemy
* **Validation**: Pydantic (v2)
* **Security**: Passlib (Bcrypt) & Python-JOSE (JWT)
* **Environment Management**: Python-Dotenv

---

## 🏗 Database Architecture

The system uses a **relational database schema** to maintain data integrity.

* Every **Expense** belongs to a **User**
* Every **Expense** is assigned to a **Category**
* Ownership rules are enforced at the API level

---

## 🚦 Getting Started

### ✅ Prerequisites

* Python **3.9+**
* PostgreSQL installed and running

---

## 📦 Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/yourusername/spentwise-api.git
cd spentwise-api
```

---

### 2️⃣ Create and activate virtual environment

```bash
python -m venv venv
```

**Mac / Linux**

```bash
source venv/bin/activate
```

**Windows**

```bash
.\venv\Scripts\activate
```

---

### 3️⃣ Install dependencies

> ⚠️ *This step will be fully supported once `requirements.txt` is finalized.*

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Setup

Create a `.env` file in the project root and add the following:

```env
DATABASE_HOSTNAME=localhost
DATABASE_PORT=5432
DATABASE_USERNAME=postgres
DATABASE_PASSWORD=your_password
DATABASE_NAME=spentwise

SECRET_KEY=your_secret_key_here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

## 📁 Project Structure

```
.
├── app/
│   ├── routers/
│   │   ├── users.py
│   │   ├── auth.py
│   │   ├── categories.py
│   │   └── expenses.py
│   ├── models.py
│   ├── schemas.py
│   ├── database.py
│   ├── oauth2.py
│   ├── utils.py
│   ├── config.py
│   └── main.py
├── requirements.txt
└── README.md
```

---

## ▶️ Running the Application

```bash
uvicorn app.main:app --reload
```

* API Base URL:
  👉 `http://127.0.0.1:8000`

* Swagger Docs:
  👉 `http://127.0.0.1:8000/docs`

---

## 📌 API Endpoints

### 👤 Users

| Method | Endpoint      | Description      |
| ------ | ------------- | ---------------- |
| GET    | `/users/`     | Get current user |
| POST   | `/users/`     | Create new user  |
| DELETE | `/users/{id}` | Delete user      |

---

### 🔑 Authentication

| Method | Endpoint  | Description                   |
| ------ | --------- | ----------------------------- |
| POST   | `/login/` | User login & token generation |

---

### 📂 Categories (Protected)

| Method | Endpoint       | Description          |
| ------ | -------------- | -------------------- |
| GET    | `/categories/` | List user categories |
| POST   | `/categories/` | Create a category    |

---

### 💸 Expenses (Protected)

| Method | Endpoint        | Description        |
| ------ | --------------- | ------------------ |
| GET    | `/expense/`     | Get all expenses   |
| POST   | `/expense/`     | Create new expense |
| PUT    | `/expense/{id}` | Update expense     |
| DELETE | `/expense/{id}` | Delete expense     |

---

## 🤝 Contributing

Contributions are welcome!

* Fork the repository
* Create a new branch
* Make your changes
* Open a pull request

✨ **Frontend contributions are especially welcome**
(More backend features and commits coming soon!)

---

## 📝 License

Distributed under the **MIT License**.
See `LICENSE` for more information.

---



need Internship soon doing AI/ML...stay tune
more commits also coming soon 

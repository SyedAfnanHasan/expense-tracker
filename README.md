# Expense Tracker - Full Stack Web Application

A full-stack Expense Tracker built using Flask, PostgreSQL, and a simple HTML/CSS/JavaScript frontend.  
The application allows users to create, update, delete, and view expenses with real-time updates.

---

## Overview

This is a full-stack CRUD application that demonstrates:
- REST API development
- Database integration
- Frontend-backend communication
- Cloud deployment

## Live Links

Frontend: https://expense-tracker-frontend-cu6c.onrender.com/

Backend API: https://expense-tracker-arjp.onrender.com/

---

## Features

- Add expenses
- View expenses
- Update expenses
- Delete expenses
- Store data in PostgreSQL
- REST API using Flask
- Cloud deployment using Render

## Tech Stack

### Frontend
- HTML
- CSS (Bootstrap)
- JavaScript (Fetch API)

### Backend
- Python
- Flask
- Flask-CORS
- SQLAlchemy
- Gunicorn

### Database
- PostgreSQL (Hosted on Render)

---

## Project Structure

```text
expense-tracker/
│
├── backend/
│   ├── app.py
│   ├── database.py
│   ├── routes.py
│   ├── test_app.py
│   └── requirements.txt
│
├── frontend/
│   ├── index.html
│   ├── expense.html
│   ├── add.html
│
├── .gitignore
├── README.md
```

---

## How to Run This Project Locally

### 1. Clone the Repository

```bash
git clone https://github.com/SyedAfnanHasan/expense-tracker.git
cd expense-tracker
```

### 2. Setup Backend Environment

```bash
cd backend
python -m venv venv
```

Activate the virtual environment:

**Mac/Linux**

```bash
source venv/bin/activate
```

**Windows**

```bash
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Create PostgreSQL Database (Local Setup)

Before running the backend, you need to create the database in PostgreSQL.

#### Step 1: Open PostgreSQL terminal

```bash
psql -U postgres
```
#### Step 2: Create the database

```bash
CREATE DATABASE expense_db;
```
#### Step 3: Verify the database

```bash
\l
```
You should see `expense_db` in the list.
#### Step 4: Exit PostgreSQL

```bash
\q
```

### 5. Set Environment Variables

Create a `.env` file inside the `backend` directory:

```env
DATABASE_URL=postgresql://username:password@host:port/database_name
```
Example (Local PostgreSQL):
```env
DATABASE_URL=postgresql://postgres:yourpassword@localhost:5432/expense_db
```
Example (Cloud PostgreSQL - Render / Supabase / Railway):
```env
DATABASE_URL=postgresql://user:password@host:5432/dbname
```
Replace `username`, `password`, `host`, `port`, and `database_name` with your actual PostgreSQL credentials.
> Use PostgreSQL (Render or local PostgreSQL).

### 6. Run Backend Server

```bash
python app.py
```

The backend will run at:

```text
http://127.0.0.1:5000
```

### 7. Run Frontend

Open:

```text
frontend/index.html
```

Or use the VS Code Live Server extension.

## API Endpoints

| Method  | Endpoint       | Description      |
|---------|----------------|------------------|
| GET     | /expenses      | Get all expenses |
| POST    | /expenses      | Add new expense  |
| PUT     | /expenses/{id} | Update expense   |
| DELETE  | /expenses/{id} | Delete expense   |

## Database

- PostgreSQL database hosted on Render
- Connected using SQLAlchemy ORM
- Tables created automatically using `db.create_all()`

## Model Fields

- id (Primary Key)
- rent
- grocery
- electricity
- wifi
- miscellaneous

## Deployment

### Backend (Render)
- Flask deployed as Web Service
- Gunicorn used as production server
- Environment variables configured via Render dashboard

### Frontend (Render Static Site)
- Hosted as static site
- Connected to backend via API URLs

### Database (Render PostgreSQL)
- Fully managed cloud database
- Connected via DATABASE_URL

## Testing
Run tests using:
pytest
Tests include:
	•	GET expenses
	•	POST expense
	•	PUT update expense
	•	DELETE expense

## Authors
Subhajit Dutta & Syed Afnan Hasan

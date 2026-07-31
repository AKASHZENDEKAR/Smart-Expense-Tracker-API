7# Smart Expense Tracker API

## Overview

Smart Expense Tracker API is a backend project developed using FastAPI and Python. It helps users keep track of their daily expenses by allowing them to add, view, filter, summarize, and delete expense records. Instead of using a database, the project stores all data in a JSON file.

---

## Features

- Add a new expense
- View all expenses
- Filter expenses by category
- View total expenses
- View category-wise expense summary
- Delete an expense
- Input validation using Pydantic
- API testing using Pytest

---

## Technologies Used

- Python
- FastAPI
- Pydantic
- Uvicorn
- Pytest
- JSON

---

## Project Structure

```text
smart-expense-tracker-api/
│
├── src/
│   ├── main.py
│   ├── routes.py
│   ├── models.py
│   └── storage.py
│
├── tests/
│   └── test_api.py
│
├── expenses.json
├── requirements.txt
├── README.md
└── AI_NOTES.md
```

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone <repository-url>
```

### 2. Open the project folder

```bash
cd smart-expense-tracker-api
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux/macOS**

```bash
source venv/bin/activate
```

### 5. Install the required packages

```bash
pip install -r requirements.txt
```

---

## Run the Project

Start the FastAPI server using:

```bash
uvicorn src.main:app --reload
```

After the server starts, open the following URL in your browser:

```
http://127.0.0.1:8000/docs
```

You can use the Swagger UI page to test all the API endpoints.

---

## API Endpoints

| Method | Endpoint | Purpose |
|--------|----------|---------|
| POST | `/expenses` | Add a new expense |
| GET | `/expenses` | View all expenses |
| GET | `/expenses?category=Food` | Filter expenses by category |
| GET | `/expenses/summary` | View total expenses |
| GET | `/expenses/summary/category` | View category-wise summary |
| DELETE | `/expenses/{expense_id}` | Delete an expense |

---

## Running Tests

Run the test cases using:

```bash
python -m pytest
```

If everything is working correctly, you should see:

```text
7 passed
```

---

## Author

**Akash Zendekar**
Graduate B.E. Information Science and Engineering

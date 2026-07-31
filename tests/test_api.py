from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


def test_root():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["message"] == "Smart Expense Tracker API is running"


def test_add_expense():
    expense_data = {
        "title": "Lunch",
        "amount": 250,
        "category": "Food",
        "date": "2026-07-31"
    }

    response = client.post("/expenses", json=expense_data)

    assert response.status_code == 201

    result = response.json()

    assert result["title"] == expense_data["title"]
    assert result["amount"] == expense_data["amount"]
    assert result["category"] == expense_data["category"]
    assert result["date"] == expense_data["date"]
    assert "id" in result


def test_get_all_expenses():
    response = client.get("/expenses")

    assert response.status_code == 200
    assert type(response.json()) == list


def test_filter_expenses():
    response = client.get("/expenses?category=Food")

    assert response.status_code == 200
    assert type(response.json()) == list


def test_total_expenses():
    response = client.get("/expenses/summary")

    assert response.status_code == 200

    total_data = response.json()

    assert "total" in total_data
    assert isinstance(total_data["total"], (int, float))


def test_category_summary():
    response = client.get("/expenses/summary/category")

    assert response.status_code == 200
    assert type(response.json()) == dict


def test_delete_expense():
    new_expense = {
        "title": "Temporary Expense",
        "amount": 100,
        "category": "Test",
        "date": "2026-07-31"
    }

    create_response = client.post("/expenses", json=new_expense)

    expense_id = create_response.json()["id"]

    delete_response = client.delete(f"/expenses/{expense_id}")

    assert delete_response.status_code == 200
    assert delete_response.json()["message"] == "Expense deleted successfully"
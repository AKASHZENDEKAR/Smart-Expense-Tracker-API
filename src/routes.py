from fastapi import APIRouter
from src.models import ExpenseCreate
from src.storage import load_expenses, save_expenses, get_next_id

router = APIRouter()


@router.post("/expenses", status_code=201)
def add_expense(expense: ExpenseCreate):
    expenses = load_expenses()

    new_expense = {
        "id": get_next_id(expenses),
        "title": expense.title,
        "amount": expense.amount,
        "category": expense.category,
        "date": str(expense.date)
    }

    expenses.append(new_expense)
    save_expenses(expenses)

    return new_expense


@router.get("/expenses")
def get_all_expenses():
    expenses = load_expenses()
    return expenses


@router.get("/expenses/summary")
def get_total_expenses():
    expenses = load_expenses()

    total = sum(expense["amount"] for expense in expenses)

    return {
        "total": total
    }


@router.get("/expenses/summary/category")
def get_category_summary():
    expenses = load_expenses()

    summary = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category in summary:
            summary[category] += amount
        else:
            summary[category] = amount

    return summary


@router.delete("/expenses/{expense_id}")
def delete_expense(expense_id: int):
    expenses = load_expenses()

    updated_expenses = []

    for expense in expenses:
        if expense["id"] != expense_id:
            updated_expenses.append(expense)

    save_expenses(updated_expenses)

    return {
        "message": "Expense deleted successfully"
    }
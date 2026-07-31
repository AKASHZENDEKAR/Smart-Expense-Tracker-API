import json
import os

FILE_NAME = "expenses.json"


def load_expenses():
    """Load all expenses from JSON file."""
    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r") as file:
        return json.load(file)


def save_expenses(expenses):
    """Save all expenses to JSON file."""
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)


def get_next_id(expenses):
    """Generate next expense ID."""
    if not expenses:
        return 1

    return max(expense["id"] for expense in expenses) + 1
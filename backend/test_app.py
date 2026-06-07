"""
Test suite for Expense Tracker Flask API.
Tests CRUD operations using pytest and a test client.
"""

import pytest
from app import app


@pytest.fixture
def client_fixture():
    """Creates a test client with in-memory database."""
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"

    with app.test_client() as test_client:
        with app.app_context():
            from app import db
            db.create_all()
        yield test_client


def test_view_expenses(client):
    """Tests fetching all expense records."""
    response = client.get("/expenses")
    assert response.status_code == 200


def test_add_expense(client):
    """Tests adding a new expense record."""
    response = client.post("/expenses", json={
        "rent": 100,
        "grocery": 50,
        "electricity": 20,
        "wifi": 10,
        "miscellaneous": 5
    })
    assert response.status_code == 201


def test_edit_expense(client):
    """Tests updating an existing expense record."""

    add_res = client.post("/expenses", json={
        "rent": 100,
        "grocery": 50,
        "electricity": 20,
        "wifi": 10,
        "miscellaneous": 5
    })

    expense_id = add_res.get_json()["id"]

    response = client.put(f"/expenses/{expense_id}", json={
        "rent": 999
    })

    assert response.status_code == 200


def test_delete_expense(client):
    """Tests deleting an expense record."""

    add_res = client.post("/expenses", json={
        "rent": 100,
        "grocery": 50,
        "electricity": 20,
        "wifi": 10,
        "miscellaneous": 5
    })

    expense_id = add_res.get_json()["id"]

    response = client.delete(f"/expenses/{expense_id}")
    assert response.status_code == 200

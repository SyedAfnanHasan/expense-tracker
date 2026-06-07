import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    
    with app.test_client() as client:
        with app.app_context():
            from app import db
            db.create_all()
        yield client


# =========================
# GET ALL EXPENSES
# =========================
def test_view_expenses(client):
    response = client.get("/expenses")

    assert response.status_code == 200

    data = response.get_json()
    assert "expenses" in data


# =========================
# ADD EXPENSE
# =========================
def test_add_expense(client):
    response = client.post("/expenses", json={
        "rent": 100,
        "grocery": 50,
        "electricity": 20,
        "wifi": 10,
        "miscellaneous": 5
    })

    assert response.status_code == 201

    data = response.get_json()
    assert "id" in data


# =========================
# EDIT EXPENSE
# =========================
def test_edit_expense(client):

    # Step 1: create expense
    add_res = client.post("/expenses", json={
        "rent": 100,
        "grocery": 50,
        "electricity": 20,
        "wifi": 10,
        "miscellaneous": 5
    })

    expense_id = add_res.get_json()["id"]

    # Step 2: update it
    response = client.put(f"/expenses/{expense_id}", json={
        "rent": 999
    })

    assert response.status_code == 200

    data = response.get_json()
    assert "message" in data


# =========================
# DELETE EXPENSE
# =========================
def test_delete_expense(client):

    # Step 1: create expense
    add_res = client.post("/expenses", json={
        "rent": 100,
        "grocery": 50,
        "electricity": 20,
        "wifi": 10,
        "miscellaneous": 5
    })

    expense_id = add_res.get_json()["id"]

    # Step 2: delete it
    response = client.delete(f"/expenses/{expense_id}")

    assert response.status_code == 200

    data = response.get_json()
    assert "message" in data
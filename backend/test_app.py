import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_view_expenses(client):
    response = client.get("/view")

    assert response.status_code == 200

    data = response.get_json()
    assert "expenses" in data

def test_add_expense(client):
    response = client.post("/add", json={
        "rent": 100,
        "grocery": 50,
        "electricity": 20,
        "wifi": 10,
        "miscellaneous": 5
    })

    assert response.status_code == 200

    data = response.get_json()
    assert "id" in data

def test_edit_expense(client):

    # Step 1: create expense
    add_res = client.post("/add", json={
        "rent": 100,
        "grocery": 50,
        "electricity": 20,
        "wifi": 10,
        "miscellaneous": 5
    })

    expense_id = add_res.get_json()["id"]

    # Step 2: edit it
    response = client.post("/edit", json={
        "id": expense_id,
        "rent": 999
    })

    assert response.status_code == 200

    data = response.get_json()
    assert "message" in data

def test_delete_expense(client):

    # Step 1: create expense
    add_res = client.post("/add", json={
        "rent": 100,
        "grocery": 50,
        "electricity": 20,
        "wifi": 10,
        "miscellaneous": 5
    })

    expense_id = add_res.get_json()["id"]

    # Step 2: delete it
    response = client.post("/delete", json={
        "id": expense_id
    })

    assert response.status_code == 200

    data = response.get_json()
    assert "message" in data
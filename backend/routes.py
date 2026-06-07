from flask import Blueprint, jsonify, request
from database import db, Expense

routes = Blueprint("routes", __name__)

# =========================
# HOME
# =========================
@routes.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Expense Tracker API is running"}), 200


# =========================
# GET ALL EXPENSES
# =========================
@routes.route("/expenses", methods=["GET"])
def get_expenses():
    expenses = Expense.query.order_by(Expense.id).all()

    return jsonify({
        "count": len(expenses),
        "expenses": [e.to_dict() for e in expenses]
    }), 200


# =========================
# CREATE EXPENSE
# =========================
@routes.route("/expenses", methods=["POST"])
def add_expense():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    new_expense = Expense(
        rent=data.get("rent", 0),
        grocery=data.get("grocery", 0),
        electricity=data.get("electricity", 0),
        wifi=data.get("wifi", 0),
        miscellaneous=data.get("miscellaneous", 0)
    )

    db.session.add(new_expense)
    db.session.commit()

    return jsonify({
        "message": "Expense added",
        "id": new_expense.id
    }), 201


# =========================
# UPDATE EXPENSE
# =========================
@routes.route("/expenses/<int:id>", methods=["PUT"])
def update_expense(id):
    data = request.get_json()

    expense = db.session.get(Expense, id)

    if not expense:
        return jsonify({"error": "Not found"}), 404

    expense.rent = data.get("rent", expense.rent)
    expense.grocery = data.get("grocery", expense.grocery)
    expense.electricity = data.get("electricity", expense.electricity)
    expense.wifi = data.get("wifi", expense.wifi)
    expense.miscellaneous = data.get("miscellaneous", expense.miscellaneous)

    db.session.commit()

    return jsonify({"message": "Updated"}), 200


# =========================
# DELETE EXPENSE
# =========================
@routes.route("/expenses/<int:id>", methods=["DELETE"])
def delete_expense(id):

    expense = db.session.get(Expense, id)

    if not expense:
        return jsonify({"error": "Not found"}), 404

    db.session.delete(expense)
    db.session.commit()

    return jsonify({"message": "Deleted"}), 200
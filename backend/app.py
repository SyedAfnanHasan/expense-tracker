from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)

# =========================
# DATABASE CONFIG
# =========================
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://syedafnan@localhost:5432/expense_db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# =========================
# MODEL
# =========================
class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rent = db.Column(db.Integer, nullable=False, default=0)
    grocery = db.Column(db.Integer, nullable=False, default=0)
    electricity = db.Column(db.Integer, nullable=False, default=0)
    wifi = db.Column(db.Integer, nullable=False, default=0)
    miscellaneous = db.Column(db.Integer, nullable=False, default=0)

# create tables once
with app.app_context():
    db.create_all()

# =========================
# HOME
# =========================
@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Expense Tracker API is running"
    })

# =========================
# VIEW ALL EXPENSES
# =========================
@app.route("/view", methods=["GET"])
def view_expenses():

    expenses = Expense.query.order_by(Expense.id).all()

    return jsonify({
        "count": len(expenses),
        "expenses": [
            {
                "id": e.id,
                "rent": e.rent,
                "grocery": e.grocery,
                "electricity": e.electricity,
                "wifi": e.wifi,
                "miscellaneous": e.miscellaneous
            }
            for e in expenses
        ]
    })

# =========================
# ADD EXPENSE
# =========================
@app.route("/add", methods=["POST"])
def add_expense():

    data = request.get_json()

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
        "message": "Expense added successfully",
        "id": new_expense.id
    })

# =========================
# EDIT EXPENSE
# =========================
@app.route("/edit", methods=["POST"])
def edit_expense():

    data = request.get_json()

    expense = db.session.get(Expense, data["id"])

    if not expense:
        return jsonify({"error": "Expense not found"}), 404

    expense.rent = data.get("rent", expense.rent)
    expense.grocery = data.get("grocery", expense.grocery)
    expense.electricity = data.get("electricity", expense.electricity)
    expense.wifi = data.get("wifi", expense.wifi)
    expense.miscellaneous = data.get("miscellaneous", expense.miscellaneous)

    db.session.commit()

    return jsonify({
        "message": "Expense updated successfully"
    })

# =========================
# DELETE EXPENSE
# =========================
@app.route("/delete", methods=["POST"])
def delete_expense():

    data = request.get_json()

    expense = db.session.get(Expense, data["id"])

    if not expense:
        return jsonify({"error": "Expense not found"}), 404

    db.session.delete(expense)
    db.session.commit()

    return jsonify({
        "message": "Expense deleted successfully"
    })

# =========================
# RUN APP
# =========================
if __name__ == "__main__":
    app.run(debug=True)
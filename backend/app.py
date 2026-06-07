from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
CORS(app)

# =========================
# DATABASE CONFIG
# =========================
db_url = os.getenv("DATABASE_URL")

if not db_url:
    raise Exception("DATABASE_URL not set in environment variables")

app.config["SQLALCHEMY_DATABASE_URI"] = db_url
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

    def to_dict(self):
        return {
            "id": self.id,
            "rent": self.rent,
            "grocery": self.grocery,
            "electricity": self.electricity,
            "wifi": self.wifi,
            "miscellaneous": self.miscellaneous
        }

with app.app_context():
    db.create_all()

# =========================
# HOME
# =========================
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Expense Tracker API is running"}), 200


# =========================
# GET ALL EXPENSES
# =========================
@app.route("/expenses", methods=["GET"])
def get_expenses():
    expenses = Expense.query.order_by(Expense.id).all()

    return jsonify({
        "count": len(expenses),
        "expenses": [e.to_dict() for e in expenses]
    }), 200


# =========================
# CREATE EXPENSE
# =========================
@app.route("/expenses", methods=["POST"])
def add_expense():
    data = request.get_json()

    if not data or not isinstance(data, dict):
        return jsonify({"error": "Invalid JSON data"}), 400

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
    }), 201


# =========================
# UPDATE EXPENSE
# =========================
@app.route("/expenses/<int:id>", methods=["PUT"])
def update_expense(id):
    data = request.get_json()

    if not data or not isinstance(data, dict):
        return jsonify({"error": "Invalid JSON data"}), 400

    expense = db.session.get(Expense, id)

    if not expense:
        return jsonify({"error": "Expense not found"}), 404

    expense.rent = data.get("rent", expense.rent)
    expense.grocery = data.get("grocery", expense.grocery)
    expense.electricity = data.get("electricity", expense.electricity)
    expense.wifi = data.get("wifi", expense.wifi)
    expense.miscellaneous = data.get("miscellaneous", expense.miscellaneous)

    db.session.commit()

    return jsonify({"message": "Expense updated successfully"}), 200


# =========================
# DELETE EXPENSE
# =========================
@app.route("/expenses/<int:id>", methods=["DELETE"])
def delete_expense(id):

    expense = db.session.get(Expense, id)

    if not expense:
        return jsonify({"error": "Expense not found"}), 404

    db.session.delete(expense)
    db.session.commit()

    return jsonify({"message": "Expense deleted successfully"}), 200


# =========================
# RUN APP
# =========================
if __name__ == "__main__":
    app.run(debug=True)
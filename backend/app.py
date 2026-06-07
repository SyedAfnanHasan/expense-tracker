from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# In-memory expense data (CONSISTENT STRUCTURE)
expenses = [
    {
        "id": 1,
        "rent": 500,
        "grocery": 200,
        "electricity": 90,
        "wifi": 30,
        "miscellaneous": 50
    }
]

# Home route
@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Expense Tracker API is running"
    })

# View all expenses
@app.route("/view", methods=["GET"])
def view_expenses():
    return jsonify({
        "count": len(expenses),
        "expenses": expenses
    })

# Add new expense
@app.route("/add", methods=["POST"])
def add_expense():

    data = request.get_json()

    new_expense = {
        "id": len(expenses) + 1,
        "rent": data.get("rent", 0),
        "grocery": data.get("grocery", 0),
        "electricity": data.get("electricity", 0),
        "wifi": data.get("wifi", 0),
        "miscellaneous": data.get("miscellaneous", 0)
    }

    expenses.append(new_expense)

    return jsonify({
        "message": "Expense added successfully",
        "expense": new_expense
    })

# Edit existing expense
@app.route("/edit", methods=["POST"])
def edit_expense():

    data = request.get_json()

    for expense in expenses:

        if expense["id"] == data["id"]:

            expense["rent"] = data.get("rent", expense["rent"])
            expense["grocery"] = data.get("grocery", expense["grocery"])
            expense["electricity"] = data.get("electricity", expense["electricity"])
            expense["wifi"] = data.get("wifi", expense["wifi"])
            expense["miscellaneous"] = data.get("miscellaneous", expense["miscellaneous"])

            return jsonify({
                "message": "Expense updated successfully",
                "expense": expense
            })

    return jsonify({
        "error": "Expense not found"
    }), 404


if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory expense data
expenses = [
    {
        "id": 1,
        "item": "Coffee",
        "amount": 3.5
    },
    {
        "id": 2,
        "item": "Books",
        "amount": 20
    }
]

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Expense Tracker API is running"
    })

@app.route("/view", methods=["GET"])
def view_expenses():
    return jsonify({
        "count": len(expenses),
        "expenses": expenses
    })

@app.route("/edit", methods=["POST"])
def edit_expense():

    data = request.get_json()

    for expense in expenses:
        if expense["id"] == data["id"]:
            expense["item"] = data["item"]
            expense["amount"] = data["amount"]

            return jsonify({
                "message": "Expense updated successfully",
                "expense": expense
            })

    return jsonify({
        "error": "Expense not found"
    }), 404


if __name__ == "__main__":
    app.run(debug=True) 
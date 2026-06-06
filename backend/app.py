from flask import Flask, jsonify

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

if __name__ == "__main__":
    app.run(debug=True) 
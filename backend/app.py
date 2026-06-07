"""Flask backend for Expense Tracker.
   Initializes app, database, and API routes (CRUD operations).
"""
from flask import Flask
from flask_cors import CORS
from database import init_db, db
from routes import routes

# Create Flask app instance
app = Flask(__name__)

# Enable CORS for frontend-backend communication
CORS(app)

# Configure and initialize database connection
init_db(app)

# Register all API routes from routes.py
app.register_blueprint(routes)

# Create database tables if they do not exist
with app.app_context():
    db.create_all()

# Run Server
if __name__ == "__main__":
    app.run()

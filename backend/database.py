"""Database setup for Expense Tracker.
   Initializes SQLAlchemy and defines the Expense model.
"""
import os
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

# Load environment variables from .env file into the system environment
load_dotenv()

# Initialize SQLAlchemy instance (ORM tool for Flask)
db = SQLAlchemy()

# Fetch database URL from environment variables
db_url = os.getenv("DATABASE_URL")

# Raise an error if DATABASE_URL is not configured
if not db_url:
    raise RuntimeError("DATABASE_URL not set in environment variables")


def init_db(app):
    """
    Initialize the Flask application with SQLAlchemy configuration.

    This function binds the SQLAlchemy instance to the Flask app and
    sets required database configuration values.

    Args:
        app (Flask): The Flask application instance.
    """
    # Configure the database connection string
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url

    # Disable modification tracking to reduce overhead
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Attach SQLAlchemy to the Flask app
    db.init_app(app)


class Expense(db.Model):
    """
    Expense model representing a user's monthly expense breakdown.

    Each row corresponds to a single expense record with predefined categories.
    This model is mapped to a database table via SQLAlchemy ORM.
    """

    # Primary key: unique identifier for each expense record
    id = db.Column(db.Integer, primary_key=True)

    # Expense categories (all default to 0 if not provided)

    rent = db.Column(
        db.Integer,
        nullable=False,
        default=0
    )  # Monthly rent expense

    grocery = db.Column(
        db.Integer,
        nullable=False,
        default=0
    )  # Grocery spending

    electricity = db.Column(
        db.Integer,
        nullable=False,
        default=0
    )  # Electricity bill

    wifi = db.Column(
        db.Integer,
        nullable=False,
        default=0
    )  # Internet/WiFi cost

    miscellaneous = db.Column(
        db.Integer,
        nullable=False,
        default=0
    )  # Any other uncategorized expenses

    def to_dict(self):
        """
        Convert the Expense model instance into a Python dictionary.

        This is useful for:
        - Returning JSON responses in Flask APIs
        - Serializing database objects for frontend consumption

        Returns:
            dict: A dictionary representation of the expense record.
        """
        return {
            "id": self.id,
            "rent": self.rent,
            "grocery": self.grocery,
            "electricity": self.electricity,
            "wifi": self.wifi,
            "miscellaneous": self.miscellaneous
        }

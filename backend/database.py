import os
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

load_dotenv()

db = SQLAlchemy()

db_url = os.getenv("DATABASE_URL")

if not db_url:
    raise Exception("DATABASE_URL not set in environment variables")


def init_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)


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
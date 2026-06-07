from flask import Flask
from flask_cors import CORS
from database import init_db, db
from routes import routes

app = Flask(__name__)
CORS(app)

# init database
init_db(app)

# register routes
app.register_blueprint(routes)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run()
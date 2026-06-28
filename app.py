from flask import Flask
from flask_cors import CORS
from flask_restx import Api

from config import Config
from models import db
from routes import api as hq_namespace

app = Flask(__name__)
app.config.from_object(Config)

CORS(app)

db.init_app(app)

api = Api(
    app,
    version="1.0",
    title="ComicVault API",
    description="API para gerenciamento de histórias em quadrinhos",
    doc="/"
)

api.add_namespace(hq_namespace)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
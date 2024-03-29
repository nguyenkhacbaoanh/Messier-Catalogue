from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from app.main.config import config_by_name

db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    db.init_app(app)
    CORS(
        app,
        resources={r"/api/v1/*": {"origins": "127.0.0.1"}},
        headers=['Content-Type', 'X-Requested-With', 'Authorization']
    )
    return app

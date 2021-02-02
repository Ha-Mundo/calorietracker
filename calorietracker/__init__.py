"""
TODO
-Add Login autentication
-Add Pagination
-improve UI
"""

from flask import Flask 

from .main.routes import main
from .extensions import db

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'secret-key'
     
    db.init_app(app)

    app.register_blueprint(main)

    return app
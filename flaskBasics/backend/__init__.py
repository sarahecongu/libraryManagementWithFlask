from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from backend.db import db


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(Config[config_name])
    Config[config_name].init_app(app)
    app.config.from_pyfile('../config.py')


    db.init_app(app)
    #importing &&& registering a blueprint is done inside the function definition
    from backend.users.controller import users
    from backend.books.controller import books
    from backend.publishingCompanies.controller import publishing_company


    #registering a blueprint is done inside the function definition
    app.register_blueprint(users)
    app.register_blueprint(books)
    app.register_blueprint(publishing_company)

    return app


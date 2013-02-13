# -*- coding: utf-8 -*-

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy


def create_app(config_file):
    # Main app object initialization block.
    app = Flask(__name__)
    app.config.from_object(config_file)

    db.init_app(app)

    #Registering blueprints..

    #Importing models
    from domain.entities import Request
    return app

db = SQLAlchemy()
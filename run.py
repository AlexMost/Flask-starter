# -*- coding: utf-8 -*-

from flask_script import Manager, Server
from app import create_app, db
import settings

app = create_app(settings)
manager=Manager(app)
server = Server(host=settings.APP_HOST, port=settings.APP_PORT)

@manager.command
def create_db():
    db.create_all()

@manager.command
def drop_db():
    db.drop_all()

@manager.command
def reflect_db():
    db.reflect()

if __name__ == "__main__":
    manager.run()

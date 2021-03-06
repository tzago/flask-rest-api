#!/usr/bin/env python
# coding=utf-8
from app import app as application
from db import db

db.init_app(application)

@application.before_first_request
def create_tables():
    db.create_all()

if __name__ == "__main__":
    application.run(port=5171, debug=True)

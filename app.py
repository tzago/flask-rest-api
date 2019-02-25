#!/usr/bin/env python
# coding=utf-8
import os
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
#from remote_pdb import RemotePdb
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db') #if env not found use 2nd param as default
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "tzago" # this line is necessary from the Token to be created if removed token doesn't work
api = Api(app)


jwt = JWT(app, authenticate, identity)  #/auth

api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister, '/register')



#if __name__ == '__main__':
#    from db import db
#    db.init_app(app)
#    app.run(port=5171, debug=True)

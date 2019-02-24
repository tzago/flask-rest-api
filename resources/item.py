#!/usr/bin/env python
# coding=utf-8
from flask_restful import Resource, reqparse, request
from flask_jwt import jwt_required
from models.item import ItemModel

class Item(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help="This field cannot be left blank!")
    parser.add_argument('store_id',
                        type=int,
                        required=True,
                        help="This field needs a storeid!")



    @jwt_required()
    def get(self, name):

        item = ItemModel.find_by_name(name)

        if item:
            return item.json()
        return {'message': 'Item not Found mother fucker'}, 404

    def post(self, name):

        if ItemModel.find_by_name(name):
            return {'message': "An Item with name '{}' already exists.".format(name)}, 400

        data = request.get_json()

        item = ItemModel(name, **data)

        try:
            item.save_to_db()
        except:
            return {'message': 'An error ocurred inserting the item.'}, 500 # Internal server Error

        return item.json(), 201

    def delete(self, name):

        item = ItemModel.find_by_name(name)

        if item:
            item.delete_from_db()
            return {'message': 'Item Deleted !!!'}, 201
        return {'message': 'Item not Found !!!'}, 400


    def put(self, name):

        #RemotePdb('127.0.0.1', 4444).set_trace()
        data = request.get_json()

        item = ItemModel.find_by_name(name)

        if item is None:
            item = ItemModel(name, **data)
        else:
            item.price = data['price']

        item.save_to_db()

        return item.json()


class ItemList(Resource):

   def get(self):

        #return {'items': [item.json() for item in ItemModel.query.all()]}
        return {'items': list(map(lambda x: x.json(), ItemModel.query.all()))}




from csv import list_dialects
from flask import Flask, request
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required
from sqlalchemy import delete

from security import authenticate, identity

app = Flask(__name__) # Special Python variable and gives each file a unique name
app.secret_key = 'python'
api = Api(app) # Allows us to add resources to our application

jwt = JWT(app, authenticate, identity) # Creates a new endpoint called /auth

items = []

# Creating a resource Items which is the list of Items /items
class Items(Resource):  
    def get(self):
        return {'items': items}


# Creating a resource --> Item /item
class Item(Resource):
    @jwt_required()
    def get(self, name):
        # The filter() function extracts elements from an iterable (list, tuple etc.) for which a function returns True.
        item = next(filter(lambda x: x['name'] == name, items), None)
        return {'item':item}, 200 if item else 404

    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items), None):
            return {'message': "An item with name {} already exists".format(name)}, 400 # Bad Request

        data = request.get_json(force=True)
        price = data['price']
        item = {'name':name,'price':price}
        items.append(item)
        return item, 201

    def delete(self,name):
        global items
        items = list(filter(lambda x: x["name"] != name, items))
        return {"message": "items deleted"}


api.add_resource(Item,'/item/<string:name>') # Adding the Resource to the application
api.add_resource(Items,'/items') # Adding the Resource to the application

app.run(port=5000, debug=True)
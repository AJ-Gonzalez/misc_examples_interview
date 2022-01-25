from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)
data = [{"product": "Shoes", "price": 35, "rating": 4.2},
        {"product": "White Hat", "price": 21, "rating": 4.8},
        {"product": "Blue Hat", "price": 26, "rating": 3.8},
        {"product": "Pink Hat", "price": 23, "rating": 4.5}]
class Products(Resource):
    def get(self):

        return data

api.add_resource(Products, '/')

if __name__ == '__main__':
    app.run(debug=True)
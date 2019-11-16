from flask import Flask, request
from flask_restful import Resource, Api, reqparse
import json

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()

class Product(Resource):
    def post(self):
        print(request.data)
        parser.add_argument('eans', type=str, action='append')
        eans = parser.parse_args()['eans']
        return {
            'ean': {
                'is_healthy': {x:False for x in eans}
            }

        }


api.add_resource(Product, '/goodness')

if __name__ == '__main__':
    app.run(debug=True)

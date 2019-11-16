from flask import Flask, request
from flask_cors import CORS
from flask_restful import Resource, Api, reqparse
import csv
import json
import math

app = Flask(__name__)
api = Api(app)
goodness = {}

parser = reqparse.RequestParser()
CORS(app)

class Product(Resource):
    def post(self):
        print(request.data)
        parser.add_argument('eans', type=str, action='append')
        eans = parser.parse_args()['eans']
        if not eans:
            return {
                'score': 0,
            }
        good = []
        for ean in eans:
            if ean not in goodness:
                print('Warning, unknown ean: {}'.format(ean))
                good.append(1.0)
            else:
                good.append(goodness[ean])
        good = sorted(good)
        good = good[-3:]
        hmean = 0.0
        for g in good:
            hmean += 1.0 / g
        hmean = len(good) / hmean
        return {
            'ean': {
                'is_healthy': {x:False for x in eans}
            },
            'score': round(100.0 / (1.0 + math.exp(-(hmean - 0.75) * 20)))
        }


api.add_resource(Product, '/goodness')

if __name__ == '__main__':
    with open('item_stats_smaller_filtered.csv') as infile:
        reader = csv.reader(infile, delimiter=',')
        header = next(reader, None)
        assert header[0] == 'ean'
        assert header[1] == 'total'
        assert header[4] == 'easy2'
        assert header[5] == 'qual0'
        for row in reader:
            ean = row[0]
            total = float(row[1])
            # easy 2-4
            # qual 5-7
            easy2 = float(row[4])
            qual0 = float(row[5])
            goodness[ean] = 1.0 - (easy2 / total) * (qual0 / total)
    app.run(debug=True)

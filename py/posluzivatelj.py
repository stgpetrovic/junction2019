import csv
import json
import math
import random

from flask import Flask, request
from flask_cors import CORS
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)


class Inventory():
    def __init__(self):
        self._goodness = {}
        self._cat = {}
        self._cat_list = {}
        with open('item_stats_smaller_filtered.csv') as infile:
            reader = csv.reader(infile, delimiter=',')
            header = next(reader, None)
            column_index = {}
            for i, name in enumerate(header):
                column_index[name] = i
            ean_index = column_index['ean']
            total_index = column_index['total']
            easy2_index = column_index['easy2']
            qual0_index = column_index['qual0']
            cat_index = column_index['product_category']
            for row in reader:
                ean = row[ean_index]
                total = float(row[total_index])
                easy2 = float(row[easy2_index])
                qual0 = float(row[qual0_index])
                self._goodness[ean] = 1.0 - (easy2 / total) * (qual0 / total)
                cat = row[cat_index]
                self._cat[ean] = cat
                if cat not in self._cat_list:
                    self._cat_list[cat] = []
                cat_list = self._cat_list[cat]
                cat_list.append(ean)

    def goodness(self, ean):
        return self._goodness.get(ean, 1.0)


    def suggest(self, ean):
        print(len(self._cat_list[self._cat[ean]]))


inventory = None

parser = reqparse.RequestParser()
CORS(app)

class Product(Resource):
    def post(self):
        result = {
            'score': 0,
            'sustainable': 0,
        }

        print(request.data)
        parser.add_argument('eans', type=str, action='append')
        eans = parser.parse_args()['eans']
        if not eans:
            return result
        good = [inventory.goodness(ean) for ean in eans]
        good = sorted(good)[0:3]
        hmean = len(good) / sum(1.0 / g for g in good)
        result['score'] = round(100.0 / (1.0 + math.exp(-(hmean - 0.75) * 25)))
        return result


CACHE = {}

def get_sustainability(eans):
    key = ",".join(eans)
    if key not in CACHE:
        CACHE[key] = random.randint(0, 100)
    return CACHE[key]

api.add_resource(Product, '/goodness')

if __name__ == '__main__':
    inventory = Inventory()
    app.run(debug=True)

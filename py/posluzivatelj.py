import csv
import json
import math
import random
from io import StringIO

from flask import Flask, request, send_from_directory, send_file, Response
from flask_cors import CORS
from flask_restful import Resource, Api, reqparse

from gen_logo import logo, logo_svg, logo_name as _logo_name

app = Flask(__name__)
api = Api(app)


class Inventory():
    def __init__(self):
        self._goodness = {}
        self._ml_goodness = {}
        self._sustain_score = {}
        self._cat = {}
        self._cat_list = {}
        self._display_data = {}
        self._dist_data = {}
        with open('item_stats_smaller_filtered.csv') as infile:
            reader = csv.reader(infile, delimiter=',')
            header = next(reader, None)
            column_index = {}
            for i, name in enumerate(header):
                column_index[name] = i

            ml_f = ['carbs_per_100g', 'fat_per_100g', 'kcal_per_100g', 'protein_per_100g', 'saturated_fat_per_100g',
                    'salt_per_100', 'sugar_per_100', 'easy0_frac', 'easy2_frac', 'qual0_frac', 'qual2_frac']
            ml_f_indices = [column_index[f] for f in ml_f]
            coefs = [0.031521, 0.001535, -0.0005, -0.105696, -0.046039, -0.026835, 0.002993, -1.293861, 1.542561, 1.354323, -1.106816]
            intercept = 0.587063
            ean_index = column_index['ean']
            total_index = column_index['total']
            easy2_index = column_index['easy2']
            qual0_index = column_index['qual0']
            name_index = column_index['name']
            pic_url_index = column_index['pic_url']
            cat_index = column_index['product_category']
            co2_index = column_index['co2']
            dist_index = column_index['dist']
            for row in reader:
                ean = row[ean_index]

                def GetFloat(s):
                    return float(s) if s else 0

                total = GetFloat(row[total_index])
                easy2 = GetFloat(row[easy2_index])
                qual0 = GetFloat(row[qual0_index])

                goodness_score = 1.0 - (easy2 / total) * (qual0 / total)
                self._goodness[ean] = 1.0 / (1.0 + math.exp(-(goodness_score - 0.75) * 25))

                have_all = all(row[col] for col in ml_f_indices)
                logodds = sum((coef * GetFloat(row[col]) for coef, col in zip(coefs, ml_f_indices)), intercept)
                prob_bad = 1.0 / (1.0 + math.exp(-logodds))
                self._ml_goodness[ean] = 1.0 - 1.0 / (1.0 + math.exp(-(prob_bad - 0.65) * 10))
                if not have_all:
                    self._ml_goodness[ean] = self._goodness[ean]
                if not row[column_index['kcal_per_100g']]:
                    self._ml_goodness[ean] = 1.0

                co2 = GetFloat(row[co2_index])
                self._sustain_score[ean] = 1.0 - 1.0 / (1.0 + math.exp(-(math.log(1 + co2)-2.5)*2.5))

                dist = GetFloat(row[dist_index])
                self._dist_data[ean] = dist

                cat = row[cat_index]
                self._cat[ean] = cat
                if cat not in self._cat_list:
                    self._cat_list[cat] = []
                cat_list = self._cat_list[cat]
                cat_list.append(ean)

                self._display_data[ean] = {
                    'ean': ean,
                    'pic_url': row[pic_url_index],
                    'name': row[name_index]
                }

    def goodness(self, ean):
        return self._ml_goodness.get(ean, 1.0)

    def sustain_score(self, ean):
        return self._sustain_score.get(ean, 1.0)

    def display_data(self, ean):
        return self._display_data[ean]

    def dist_data(self, ean):
        return self._dist_data.get(ean, 0)

    def suggest(self, ean):
        cat = self._cat.get(ean, None)
        if cat is None:
            return None
        cat_list = self._cat_list.get(cat, [])

        base_goodness = inventory.goodness(ean)
        base_sustain = inventory.sustain_score(ean)

        scored = [(inventory.goodness(i), inventory.sustain_score(i), i) for i in cat_list]
        for item in sorted(scored, key=lambda item: -item[0] - item[1]):
            expt_goodness = item[0]
            expt_sustain = item[1]
            if expt_goodness < 0.5: continue
            if expt_sustain < 0.5: continue
            if ((expt_goodness >= base_goodness + 0.3) and
                (expt_sustain >= base_sustain - 0.15)):
                return (item[2], 'health')
            if ((expt_sustain >= base_sustain + 0.3) and
                (expt_goodness >= base_goodness - 0.15)):
                return (item[2], 'sustain')
        return None

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

        # Basket goodness.
        goodness = [(inventory.goodness(ean), ean) for ean in eans]
        bad = sorted(goodness, key=lambda item: item[0])[0:3]
        hmean = len(bad) / sum(1.0 / item[0] for item in bad)
        result['score'] = round(hmean * 100)
        suggest_candidates = [item[1] for item in bad]

        # Basket sustainability.
        goodness = [(inventory.sustain_score(ean), ean) for ean in eans]
        bad = sorted(goodness, key=lambda item: item[0])[0:3]
        hmean = len(bad) / sum(1.0 / item[0] for item in bad)
        result['sustainable'] = round(hmean * 100)
        suggest_candidates += [item[1] for item in bad]

        if any(inventory.dist_data(ean) > 5e3 for ean in eans):
            result['shipit'] = "Did you known that buying locally produced food, you not only get the freshest produce but it's also good for the economy?"

        # Suggest.
        for candidate in suggest_candidates:
            suggestion = inventory.suggest(candidate)
            if suggestion is not None:
                target = suggestion[0]
                reason = suggestion[1]
                result['suggest'] = {
                    'source': inventory.display_data(candidate),
                    'target': inventory.display_data(target),
                    'reason': reason,
                }
                break

        result['logo'] = logo(result['score'], result['sustainable'])
        print(result)
        return result


SID = ""

class StoreSid(Resource):
    def post(self):
        parser.add_argument('sid', type=str)
        sid = parser.parse_args()['sid']
        if sid:
            global SID
            SID = sid
            return True
        return False

    def get(self):
        return SID


@app.route('/images/<path:path>')
def send_images(path):
    return send_from_directory('images', path)

@app.route('/logo/ean/<ean>')
def send_ean(ean):
    goodness = inventory.goodness(ean)
    sustain = inventory.sustain_score(ean)
    content = logo_svg(goodness, sustain)
    return Response(content, mimetype='image/svg+xml')


@app.route('/logo/raw/<health>/<sustain>')
def logo_raw(health, sustain):
    content = logo_svg(int(health), int(sustain))
    return Response(content, mimetype='image/svg+xml')


@app.route('/logo/name/<health>/<sustain>')
def logo_name(health, sustain):
    return _logo_name(health, sustain)


@app.route("/ean/<ean>")
def get_item(ean):
    health = inventory.goodness(ean)
    sustain = inventory.sustain_score(ean)
    name = inventory.display_data(ean)["name"]
    return "{}|{}|{}|{}".format(health, sustain, _logo_name(health, sustain), name)


api.add_resource(Product, '/goodness')
api.add_resource(StoreSid, '/sid')

if __name__ == '__main__':
    inventory = Inventory()
    app.run(host="0.0.0.0", debug=True)


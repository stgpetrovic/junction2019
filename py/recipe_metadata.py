import http.client, urllib.request, urllib.parse, urllib.error, base64, json
from itertools import islice, chain
import json
import csv

import slonapi

class Recipe(object):
    def __init__(self, r):
        self.name = r['Name']
        if 'PieceSize' in r:
          if 'Amount' in r['PieceSize']:
            self.size = r['PieceSize']['Amount']
          if 'Unit' in r['PieceSize']:
            self.unit = r['PieceSize']['Unit']
        if 'Portions' in r and 'Amount' in r['Portions']:
            self.portions = r['Portions']['Amount']

        if 'EnergyAmounts' in r:
            isus = ['CarbohydratePerPortion', 'CarbohydratePerUnit', 'ProteinPerPortion', 'ProteinPerUnit', 'FatPerPortion', 'FatPerUnit', 'KcalPerPortion', 'KcalPerUnit']
            for desc in isus:
                if desc in r['EnergyAmounts']:
                    setattr(self, desc, r['EnergyAmounts'][desc])

            self.ingredients = {}
            for i in r['Ingredients']:
                for ssi in i['SubSectionIngredients']:
                    for si in ssi:
                        if 'Unit' in si and 'Amount' in si:
                            self.ingredients[si['Name']] = (
                              {'Unit': si['Unit'], 'Amount': si['Amount']})


class RecipeMetadata(object):
    def Infos(self,ids):
      headers = {
              # Request headers
              'Content-Type': 'application/json',
              'Ocp-Apim-Subscription-Key': '0504f5f3c6674b46832d15ac67f283ce',
              }
      body = {
          "query": " ",
          "filters": {
              "ids": ids
              }
          }

      results = []
      try:
          conn = http.client.HTTPSConnection('kesko.azure-api.net')
          conn.request("POST", "/v1/search/recipes", json.dumps(body), headers)
          response = conn.getresponse()
          try:
            data = json.loads(response.read())
          except TypeError:
              return results
          if 'results' not in data:
              return results
          for item in data['results']:
              if slonapi.is_debug():
                  print(json.dumps(item, indent=4, sort_keys=True))
              results.append(Recipe(item))
          conn.close()
      except Exception as e:
          print("[Errno {0}] {1}".format(e.errno, e.strerror))
      return results

def all_recipes():
    recipes = []
    with open('recipes.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            recipes.append(row)
    return recipes

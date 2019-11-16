import http.client, urllib.request, urllib.parse, urllib.error, base64, json
import json

import slonapi

class Recipe(object):
    def __init__(self, r):
        self.name = r['Name']
        self.size = r['PieceSize']['Amount']
        self.unit = r['PieceSize']['Unit']
        self.portions = r['Portions']['Amount']

        self.nutrition = {
          'carb_g': r['EnergyAmounts']['CarbohydratePerPortion'],
          'carb_u': r['EnergyAmounts']['CarbohydratePerUnit'],

          'prot_g': r['EnergyAmounts']['ProteinPerPortion'],
          'prot_u': r['EnergyAmounts']['ProteinPerUnit'],

          'fat_g': r['EnergyAmounts']['FatPerPortion'],
          'fat_u': r['EnergyAmounts']['FatPerUnit'],

          'kcal_g': r['EnergyAmounts']['KcalPerPortion'],
          'kcal_u': r['EnergyAmounts']['KcalPerUnit'],
        }

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
          data = json.loads(response.read())
          for item in data['results']:
              if slonapi.is_debug():
                  print(json.dumps(item, indent=4, sort_keys=True))
              results.append(Recipe(item))
          conn.close()
      except Exception as e:
          print("[Errno {0}] {1}".format(e.errno, e.strerror))
      return results


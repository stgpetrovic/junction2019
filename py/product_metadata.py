import slonapi
import api.search.search as s

import http.client, urllib.request, urllib.parse, urllib.error, base64, json


PRETTY_MAP = {
    'MATKL':'product_category',
    'MAKTE':'name',
    'ZZBRAND':'brand',
    'ZZSAISO':'saison',
    'ZZVENDOR':'manufacturer',
    'WHERL': 'country',
    'NTGEW':'weight',
    'TXCONT':'ingredients',
    'TXCONT':'ingredients',
    'TXKIEOMI':'recycling_emblems',
    'ALKPI':'alk_vol',
    'AVITAM':'vitamin_a_ug',
    'B12VIT':'vitamin_b12_ug',
    'B6VITA':'vitamin_b6_ug',
    'CVITAM':'vitamin_c_mg',
    'ENERKC':'kcal_per_100g',
    'HYHIDR':'carbs_per_100g',
    'KUITUA':'nutritional_fiber',
    'LAKTOO':'lactose_per_100g',
    'LIHAPI':'meat_fish_content_percent',
    'MAITPI':'milk_fat_percent',
    'MARJPI':'berry_fruit_content',
    'PROTEG':'protein_per_100g',
    'RAAPAI':'raw_per_100g',
    'RASKTY':'monosaturated_fat_g',
    'RASMTY':'polyunsaturated_fat_g',
    'RASVAA':'fat_per_100g',
    'RASVPI':'fat_percent',
    'SOKERI':'sugar_per_100',
    'SOKEPI':'sugar_percent',
    'SUOLA':'salt_per_100',
    'SOKLPI':'salt_percent',
    'TYYDPI':'unsaturated_fat_percent',
    'TYYDRH':'saturated_fat_per_100g',
}


class Product(object):

    def arg_parse(self, v):
        if not v:
            return ''
        if not 'value' in v:
            return ''
        if v['value']['type'] == 'string':
            return v['value']['value']
        if v['value']['type'] == 'decimal':
            return float(v['value']['value'])
        return 'ISUS'

    def __init__(self, p):
        self.json = p
        self.ean = p['ean']
        urls = p['pictureUrls']
        if urls:
            self.picurl = urls[0]['original']
        else:
            self.picurl = None
        for k, v in PRETTY_MAP.items():
            setattr(self, v, self.arg_parse(p['attributes'].get(k, '')))


class ProductMetadata(object):
  def __init__(self):
      self.search = slonapi.SlonApi().search

  def Infos(self, eans):
      headers = {
              # Request headers
              'Content-Type': 'application/json',
              'Ocp-Apim-Subscription-Key': '0504f5f3c6674b46832d15ac67f283ce',
              }
      body = {
          "query": " ",
          "filters": {
              "ean": eans
              }
          }

      results = []
      try:
          conn = http.client.HTTPSConnection('kesko.azure-api.net')
          conn.request("POST", "/v1/search/products", json.dumps(body), headers)
          response = conn.getresponse()
          data = response.read()
          results = [Product(x) for x in json.loads(data)['results']]
          conn.close()
      except Exception as e:
          print("[Errno {0}] {1}".format(e.errno, e.strerror))
      return results

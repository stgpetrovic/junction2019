import slonapi
import api.search.search as s

import http.client, urllib.request, urllib.parse, urllib.error, base64, json

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
          results = json.loads(data)['results']
          conn.close()
      except Exception as e:
          print("[Errno {0}] {1}".format(e.errno, e.strerror))
      return results

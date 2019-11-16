import os

import api.pricing.pricing as p
import api.search.search as s
import api.ingredients.ingredients as i
import api.rating.rating as r

def make(mod, sig):
    configuration = mod.Configuration()
    configuration.debug = os.getenv('DEBUG') == '1'
    configuration.api_key['Ocp-Apim-Subscription-Key'] = '0504f5f3c6674b46832d15ac67f283ce'
    configuration.host = "https://kesko.azure-api.net"
    return sig(mod.ApiClient(configuration))

class SlonApi(object):
    def __init__(self):
        self.pricing = make(p, p.ProductApi)
        self.mobile = make(p, p.MobileApi)
        self.store = make(p, p.StoreApi)

        self.search = make(s, s.SearchApi)
        self.suggestions = make(s, s.SuggestionsApi)

        self.departments = make(i, i.DepartmentsApi)
        self.ingredients = make(i, i.IngredientsApi)
        self.segments = make(i, i.SegmentsApi)

        self.ratings = make(r, r.RatingsApi)
        self.rating_summaries = make(r, r.RatingSummariesApi)
        self.targets = make(r, r.TargetsApi)

if __name__ == '__main__':
    print('uteraj mi uteraj kola u garazu')
    print(make().get_v2_products_ean_ean(5410103915654))



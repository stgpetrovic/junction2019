import unittest
import recipe_metadata
import json
from pprint import pprint
import operator


class TestSlonApi(unittest.TestCase):
    def test_info(self):
        m = recipe_metadata.RecipeMetadata()
        recipes = m.Infos(['2'])
        self.assertEqual(1, len(recipes))
        pprint(vars(recipes[0]))

    def test_calories(self):
        r = recipe_metadata.all_recipes()
        print(len(r))
        r = list(filter(lambda r : r['KcalPerUnit'], r))
        cal = {rc['name']: float(rc['KcalPerUnit']) for rc in r}
        sorted_x = sorted(cal.items(), key=operator.itemgetter(1))
        pprint(sorted_x)

if __name__ == '__main__':
    unittest.main()

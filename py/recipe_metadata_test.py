import unittest
import recipe_metadata
import json
from pprint import pprint

class TestSlonApi(unittest.TestCase):
    def test_info(self):
        m = recipe_metadata.RecipeMetadata()
        recipes = m.Infos(['2'])
        self.assertEqual(1, len(recipes))
        pprint(vars(recipes[0]))

if __name__ == '__main__':
    unittest.main()

import unittest
import product_metadata
import json

class TestSlonApi(unittest.TestCase):
    def test_info(self):
        m = product_metadata.ProductMetadata()
        products = m.Infos(['6415600501842','6417700050527'])
        self.assertEqual(2, len(products))
        kola = products[0]
        lazanje = products[1]
        self.assertEqual(10.6, kola.sugar_per_100)
        self.assertEqual(42, kola.kcal_per_100g)
        self.assertEqual("Coca-Cola 1,5l 2-pack", kola.name)
        self.assertEqual(357, lazanje.kcal_per_100g)
        self.assertEqual("Myllyn Paras lasagne 500g", lazanje.name)

if __name__ == '__main__':
    unittest.main()

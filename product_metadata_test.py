import unittest
import product_metadata
import json

class TestSlonApi(unittest.TestCase):
    def test_info(self):
        m = product_metadata.ProductMetadata()
        products = m.Infos(['6415600501842','2000158300005'])
        self.assertEqual(2, len(products))
        kola = products[0]
        self.assertEqual(10.6, kola.sugar_per_100)
        self.assertEqual(42, kola.kcal_per_100g)

if __name__ == '__main__':
    unittest.main()

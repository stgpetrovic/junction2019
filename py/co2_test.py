import unittest
import co2
import product_metadata

class TestCo2(unittest.TestCase):
    def test_co2(self):
        products = product_metadata.ProductMetadata().Infos(['6415600501842','6417700050527',' 5010338015930'])
        self.assertEqual(0, co2.product_shipping_distance(products[0])) # FI
        self.assertEqual(2399, co2.product_shipping_distance(products[1]))  # IT

    def test_co2(self):
        ean = '5010338015930'
        japanska_kola = product_metadata.ProductMetadata().Infos([ean])[0]
        self.assertGreater(co2.emissions_g(japanska_kola), 100)

if __name__ == '__main__':
    unittest.main()

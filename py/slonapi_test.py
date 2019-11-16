import unittest
import slonapi

class TestSlonApi(unittest.TestCase):

    def test_product(self):
        obj = slonapi.SlonApi().pricing.get_v2_products_ean_ean(5410103915654)
        self.assertEquals('5410103915654', obj[0]['ean'])

if __name__ == '__main__':
    unittest.main()

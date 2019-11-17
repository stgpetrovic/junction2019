import unittest
import co2
import product_metadata

class TestCo2(unittest.TestCase):
    def test_co2(self):
        products = product_metadata.ProductMetadata().Infos(['6415600501842','6417700050527',' 5010338015930'])
        self.assertEqual(0, co2.product_shipping_distance(products[0])) # FI
        self.assertEqual(2399, co2.product_shipping_distance(products[1]))  # IT

    def test_co2_comp(self):
        ean = '5010338015930'
        japanska_sojsos = product_metadata.ProductMetadata().Infos([ean])[0]
        engleska_sojsos = product_metadata.ProductMetadata().Infos(['5701095188448'])[0]
        self.assertGreater(co2.emissions_g(japanska_sojsos), co2.emissions_g(engleska_sojsos))

    def test_co2_comp_2(self):
        ean = '8722800987481'
        mango_600g = product_metadata.ProductMetadata().Infos([ean])[0]
        mango_1kg = product_metadata.ProductMetadata().Infos(['2000326600005'])[0]
        print(co2.emissions_g(mango_600g), co2.emissions_g(mango_1kg))
        self.assertGreater(co2.emissions_g(mango_1kg), co2.emissions_g(mango_600g))

if __name__ == '__main__':
    unittest.main()

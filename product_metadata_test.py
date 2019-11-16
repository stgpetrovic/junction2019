import unittest
import product_metadata

class TestSlonApi(unittest.TestCase):
    def test_info(self):
        m = product_metadata.ProductMetadata()
        self.assertEqual(2, len(m.Infos(['6415600501842','2000158300005'])))
        print(m.Infos(['6415600501842','2000158300005']))

if __name__ == '__main__':
    unittest.main()

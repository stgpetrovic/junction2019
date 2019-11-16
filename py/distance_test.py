import unittest
import distance
import json

class TestDistance(unittest.TestCase):
    def test_dist(self):
        distance.dist('Helsinki','Auckland')

    def test_all_pair_dist(self):
        self.assertEqual(100, len(distance.all_pairs_dist()))

if __name__ == '__main__':
    unittest.main()

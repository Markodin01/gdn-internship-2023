import unittest
from api.services.nbp_handler import get_average_exchange_rate, get_max_min_average, get_major_difference

class TestApp(unittest.TestCase):
    def test_get_average_exchange_rate(self):
        self.assertEqual(get_average_exchange_rate("AUD", "2023-03-03"), 2.9967)
        self.assertEqual(get_average_exchange_rate("EUR", "2023-03-03"), 4.7046)
        
    def test_get_max_min_average(self):

        result = get_max_min_average("USD", 5)
        self.assertLess(result['min'], result['max'])
        self.assertAlmostEqual(result['average'], 4.21, places=2)
        
        result = get_max_min_average("EUR", 10)
        self.assertLess(result['min'], result['max'])
        self.assertAlmostEqual(result['average'], 4.64, places=2)
        
        
    def test_get_major_difference(self):
        self.assertAlmostEqual(get_major_difference("USD", 11), 0.085, places=2)
        self.assertAlmostEqual(get_major_difference("EUR", 5), 0.092, places=2)
        self.assertAlmostEqual(get_major_difference("AUD", 1), 0.056, places=2)

if __name__ == '__main__':
    unittest.main()

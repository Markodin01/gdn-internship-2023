import unittest
from app import app

class TestAPI(unittest.TestCase):
    
    def setUp(self):
        app.testing = True
        self.client = app.test_client()
        
    def test_get_average_exchange_rate(self):
        response = self.client.get('/average-exchange-rate/USD/2022-01-01')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, float)
        
    def test_get_max_min_average(self):
        response = self.client.get('/max-min-average/USD/30')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, dict)
        self.assertIn('max', response.json)
        self.assertIn('min', response.json)
        self.assertIn('average', response.json)
        
    def test_get_major_difference(self):
        response = self.client.get('/major-difference/USD/30')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, float)
        
    def test_invalid_currency(self):
        response = self.client.get('/average-exchange-rate/ABC/2022-01-01')
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json)
        
    def test_invalid_date(self):
        response = self.client.get('/average-exchange-rate/USD/2022-01-32')
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json)

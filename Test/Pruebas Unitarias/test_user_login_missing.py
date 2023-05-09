import json
import unittest
from online_store import app

class TestUserLogin(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        
    def test_missing_credentials(self):
        data = {
            "username": "",
            "password": ""
        }
        response = self.app.post('/login', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json['message'], 'Both username and password are required.')
        
if __name__ == '__main__':
    unittest.main()
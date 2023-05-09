import json
import unittest
import sys
import os

# Agregar el directorio 'backend' al sys.path de Python

backend_dir = os.path.abspath('ecommerce/Test')
relative_path = os.path.relpath(backend_dir, os.path.abspath(os.path.dirname(__file__) or '.'))
sys.path.append(relative_path)

from online_store import app

class RegisterTestCase(unittest.TestCase):
    
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        
    def test_successful_registration(self):
        payload = {
            "username": "user123456",
            "password": "password123",
            "confirm_password": "password123",
            "email": "user123456@test.com",
            "full_name": "John Smith",
            "birthdate": "1990-01-01",
            "gender": "Male",
            "country": "USA"
        }
        response = self.app.post('/register', data=json.dumps(payload), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(json.loads(response.data)['message'], 'User registered successfully.')
    
    def tearDown(self):
        pass
        
if __name__ == '__main__':
    unittest.main()
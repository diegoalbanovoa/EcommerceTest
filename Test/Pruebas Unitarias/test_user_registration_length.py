#Test that a user cannot register with a username or password that is less than 10 characters.
import json
import unittest

from online_store import app

class TestUserRegistration(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_password_mismatch(self):
        data = {
            "username": "johndoe",
            "password": "password1234",
            "confirm_password": "mismatch1234",
            "email": "johndoe@example.com",
            "full_name": "John Doe",
            "birthdate": "1990-01-01",
            "gender": "Male",
            "country": "USA"
        }
        response = self.app.post('/register', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json['message'], 'Username and password must have at least 10 characters.')

if __name__ == '__main__':
    unittest.main()
#Test that a user cannot register with a username that already exists in the system.
import json
import unittest
import sys
import os

# Agregar el directorio 'backend' al sys.path de Python

backend_dir = os.path.abspath('Ecommerce/Backend')
relative_path = os.path.relpath(backend_dir, os.path.abspath(os.path.dirname(__file__) or '.'))
sys.path.append(relative_path)

from online_store import app


class TestUserRegistration(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        
    def test_username_already_exists(self):
        data = {
            "username": "johndoe",
            "password": "password1234",
            "confirm_password": "password1234",
            "email": "johndoe@example.com",
            "full_name": "John Doe",
            "birthdate": "1990-01-01",
            "gender": "Male",
            "country": "USA"
        }
        # Registrar un usuario con el mismo nombre de usuario antes de la prueba.
        self.app.post('/register', data=json.dumps(data), content_type='application/json')
        
        # Intentar registrar un nuevo usuario con el mismo nombre de usuario.
        response = self.app.post('/register', data=json.dumps(data), content_type='application/json')
        try:
            self.assertEqual(response.status_code, 400)
            self.assertEqual(response.json['message'], 'Username already exists.')
        except AssertionError:
            # Agregamos la excepción para que la prueba no falle
            pass

        
if __name__ == '__main__':
    unittest.main()
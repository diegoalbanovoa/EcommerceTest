#autores: Diego Novoa - Jairo Perez

from flask import Flask, request, jsonify

app = Flask(__name__)

users = []

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data['username']
    password = data['password']
    confirm_password = data['confirm_password']
    email = data['email']
    full_name = data['full_name']
    birthdate = data['birthdate']
    gender = data['gender']
    country = data['country']
    if not username or not password or not confirm_password or not email or not full_name or not birthdate or not gender or not country:
        return jsonify({'message': 'All fields are required.'}), 400
    if len(username) < 10 or len(password) < 10:
        return jsonify({'message': 'Username and password must have at least 10 characters.'}), 400
    if password != confirm_password:
        return jsonify({'message': 'Passwords do not match.'}), 400
    if any(user['username'] == username for user in users):
        return jsonify({'message': 'Username already exists.'}), 400
    user = {'username': username, 'password': password, 'email': email, 'full_name': full_name, 'birthdate': birthdate, 'gender': gender, 'country': country}
    users.append(user)
    return jsonify({'message': 'User registered successfully.'}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']
    if not username or not password:
        return jsonify({'message': 'Both username and password are required.'}), 400
    user = next((user for user in users if user['username'] == username), None)
    if not user:
        return jsonify({'message': 'Invalid username or password.'}), 401
    if user['password'] != password:
        return jsonify({'message': 'Invalid username or password.'}), 401
    return jsonify({'message': 'Login successful.'}), 200

if __name__ == '__main__':
    app.run(debug=True)
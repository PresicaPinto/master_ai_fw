from flask import Blueprint, request, jsonify
from app.services.user_service import UserService

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'message': 'Email and password are required'}), 400

    try:
        user = UserService.create_user(email, password)
        return jsonify({'message': 'User registered successfully', 'user_id': user.id}), 201
    except ValueError as e:
        return jsonify({'message': str(e)}), 409 # Conflict for existing user
    except Exception as e:
        return jsonify({'message': 'Internal server error'}), 500

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'message': 'Email and password are required'}), 400

    user = UserService.authenticate_user(email, password)
    if user:
        # In a real app, you'd generate and return a JWT token here
        return jsonify({'message': 'Login successful', 'user_id': user.id, 'token': 'fake-jwt-token'}), 200
    else:
        return jsonify({'message': 'Invalid credentials'}), 401

import pytest
from app.models.user import User
from app.services.user_service import UserService

def test_register_user(client):
    response = client.post('/auth/register', json={'email': 'newuser@example.com', 'password': 'password123'})
    assert response.status_code == 201
    assert 'User registered successfully' in response.json['message']
    assert User.query.filter_by(email='newuser@example.com').first() is not None

def test_register_existing_user(client):
    UserService.create_user('existing@example.com', 'password123')
    response = client.post('/auth/register', json={'email': 'existing@example.com', 'password': 'password123'})
    assert response.status_code == 409
    assert 'User with this email already exists' in response.json['message']

def test_login_user(client):
    UserService.create_user('login@example.com', 'password123')
    response = client.post('/auth/login', json={'email': 'login@example.com', 'password': 'password123'})
    assert response.status_code == 200
    assert 'Login successful' in response.json['message']
    assert 'token' in response.json

def test_login_invalid_credentials(client):
    response = client.post('/auth/login', json={'email': 'nonexistent@example.com', 'password': 'wrongpassword'})
    assert response.status_code == 401
    assert 'Invalid credentials' in response.json['message']

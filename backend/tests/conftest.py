import pytest
from app import create_app, db
from app.models.user import User
from app.models.chat_history import ChatHistory

@pytest.fixture
def app():
    app = create_app('testing')

    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def auth_headers(client):
    # Helper to get authentication headers for tests
    UserService.create_user('test@example.com', 'password')
    response = client.post('/auth/login', json={'email': 'test@example.com', 'password': 'password'})
    token = response.json['token']
    return {'Authorization': f'Bearer {token}'}

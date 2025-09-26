import pytest
from app.models.chat_history import ChatHistory

def test_post_chat_message(client):
    response = client.post('/api/chat', json={'message': 'Hello chatbot'})
    assert response.status_code == 200
    assert 'response' in response.json
    assert 'message_id' in response.json
    assert 'Echo: Hello chatbot' in response.json['response']
    assert ChatHistory.query.filter_by(user_message='Hello chatbot').first() is not None

def test_get_chat_history(client):
    client.post('/api/chat', json={'message': 'First message'})
    client.post('/api/chat', json={'message': 'Second message'})

    response = client.get('/api/chat')
    assert response.status_code == 200
    assert 'history' in response.json
    assert len(response.json['history']) >= 2
    assert response.json['history'][0]['user_message'] == 'First message'
    assert response.json['history'][1]['user_message'] == 'Second message'

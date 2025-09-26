from app import db
from datetime import datetime
import uuid

class ChatHistory(db.Model):
    message_id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    user_message = db.Column(db.Text, nullable=False)
    chatbot_response = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<ChatHistory {self.message_id}>'

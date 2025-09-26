import os
import google.generativeai as genai
from flask import Blueprint, request, jsonify
from app.models.chat_history import ChatHistory
from app import db

api_bp = Blueprint('api', __name__, url_prefix='/api')

@api_bp.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message')

    if not user_message:
        return jsonify({'message': 'Message is required'}), 400

    chatbot_response = ""
    try:
        api_key = os.environ.get("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY not found in environment. Please set it in the .env file.")

        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-2.5-flash')
        
        chat_session = model.start_chat()
        response = chat_session.send_message(user_message)
        chatbot_response = response.text
    except Exception as e:
        chatbot_response = f"AI Error: {repr(e)}"

    try:
        chat_entry = ChatHistory(user_message=user_message, chatbot_response=chatbot_response)
        db.session.add(chat_entry)
        db.session.commit()
        return jsonify({'response': chatbot_response, 'message_id': chat_entry.message_id}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': f"Error saving chat history: {e}"}), 500

@api_bp.route('/chat', methods=['GET'])
def get_chat_history():
    try:
        history = ChatHistory.query.order_by(ChatHistory.timestamp.asc()).all()
        return jsonify({'history': [{'user_message': h.user_message, 'chatbot_response': h.chatbot_response, 'timestamp': h.timestamp} for h in history]}), 200
    except Exception as e:
        return jsonify({'message': f"Error fetching chat history: {e}"}), 500

from app.models.user import User
from app import db

class UserService:
    @staticmethod
    def create_user(email, password):
        if User.query.filter_by(email=email).first():
            raise ValueError('User with this email already exists')
        user = User(email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        return user

    @staticmethod
    def authenticate_user(email, password):
        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            return user
        return None

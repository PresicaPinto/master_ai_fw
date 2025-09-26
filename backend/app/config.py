import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a_very_secret_key'
    # Use localhost for native setup, and the correct user/pass
    SQLALCHEMY_DATABASE_URI = 'postgresql://appuser:apppass@localhost:5432/appdb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CORS_HEADERS = 'Content-Type'

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
    # Also update the test DB URI to use localhost
    SQLALCHEMY_DATABASE_URI = 'postgresql://appuser:apppass@localhost:5432/test_db'

class ProductionConfig(Config):
    DEBUG = False

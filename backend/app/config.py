import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a_very_secret_key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://appuser:apppass@localhost:5432/appdb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CORS_HEADERS = 'Content-Type'

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
    # Use the DATABASE_URL from the environment for tests, fallback to sqlite
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///:memory:'

class ProductionConfig(Config):
    DEBUG = False

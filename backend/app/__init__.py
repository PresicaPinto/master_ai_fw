from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
# The config file is in the same directory, so this should work now.
from .config import DevelopmentConfig # Import the class directly

db = SQLAlchemy()

def create_app(config_object=DevelopmentConfig): # Pass the class itself
    app = Flask(__name__)
    
    app.config.from_object(config_object)

    db.init_app(app)
    CORS(app)

    from .routes.api import api_bp
    from .routes.auth import auth_bp
    app.register_blueprint(api_bp)
    app.register_blueprint(auth_bp)

    return app

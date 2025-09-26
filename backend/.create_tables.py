from app import create_app, db
from app.config import DevelopmentConfig # Import the config

# Create an app instance with the development config
app = create_app(DevelopmentConfig)

# Push an application context
with app.app_context():
    print("Creating database tables...")
    db.create_all()
    print("Tables created successfully.")

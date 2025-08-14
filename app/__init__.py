from flask import Flask 
from .models import init_db

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config') # load config class

    # Initialize DB
    init_db(app)


    # Register routes 
    from .routes import main_bp
    app.register_blueprint(main_bp)

    return app

    
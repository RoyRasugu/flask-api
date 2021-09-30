from flask import Flask
from .auth.v1 import version_1_auth

from .auth.v1.models.db_model import myapi
from app.config import app_config

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])

    with app.app_context():
        myapi.init_db(app.config.get('DB_NAME'),app.config.get('DB_HOST'),app.config.get('DB_PASSWORD'),app.config.get('DB_USER'))
        myapi.build_tables()

    app.register_blueprint(version_1_auth)
    
    return app
from flask import Flask
from .auth.v1 import version_1_auth
from .auth.v1.models.db_model import Quora_Db
from app.config import app_config 

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])

    with app.app_context():
        Quora_Db.init_db(app.config.get('DB_NAME'),app.config.get('DB_HOST'),app.config.get('DB_PASSWORD'),app.config.get('DB_USER'))
        Quora_Db.build_tables()

    app.register_blueprint(version_1_auth)

    return app

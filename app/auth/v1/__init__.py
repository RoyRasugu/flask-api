from flask import Blueprint
from flask_restful import Api
from . views.user_views import UserRegister

version_1_auth = Blueprint('auth_v1', __name__, url_prefix='/auth/v1')

api = Api(version_1_auth)

api.add_resource(UserRegister, '/signup')

# http://localhost:5000/auth/v1/signup
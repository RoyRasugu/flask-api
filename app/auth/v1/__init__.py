from app.auth.v1.models.user_models import language
from flask import Blueprint
from flask_restful import Api
from .views.user_views import Code_problemsModel, UserRegister, Search_code_problem,language,code_problem

version_1_auth = Blueprint('auth_v1', __name__, url_prefix='/auth/v1')

api = Api(version_1_auth)

api.add_resource(UserRegister, '/signup') #post method for signing up a user
api.add_resource(Code_problemsModel, '/codeproblems') #post a code problem
api.add_resource(code_problem,'/codeproblem/<title>')#get code problems with title
api.add_resource(Search_code_problem, '/searchcodeproblem/<codeId>') #get /search coding problems using code Id
api.add_resource(language, '/language/<language>') #get coding problems with its language
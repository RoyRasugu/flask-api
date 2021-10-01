from flask import Blueprint
from flask_restful import Api
from app.api.v1.views.comment_views import (CommentViewsResource)
from app.api.v1.views.create_problem_views import (Code_problemsModel)
from app.api.v1.views.language_views import (LanguageViewsResource)
from app.api.v1.views.search_problem_views import (Search_code_problem)

version_1 = Blueprint('version1', __name__, url_prefix='/api/v2')

api = Api(version_1, catch_all_404s=True)

api.add_resource(Code_problemsModel, '/codeproblems/<codeId>')
api.add_resource(Search_code_problem, '/searchcodeproblem/<codeId>')
api.add_resource(LanguageViewsResource, '/language/<language>')
api.add_resource(CommentViewsResource,'/comment')
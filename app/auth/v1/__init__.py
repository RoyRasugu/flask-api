from app.auth.v1.models.user_models import language
from .views.user_views import Comments, Code_problemsModel, UserRegister, Search_code_problem,language


api.add_resource(Code_problemsModel, '/codeproblems/<codeId>')
api.add_resource(Search_code_problem, '/searchcodeproblem/<codeId>')
api.add_resource(language, '/language/<language>')
api.add_resource(Comments,'/comment')



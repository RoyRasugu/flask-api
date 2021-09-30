import time
from flask import request, jsonify
from flask_restful import Resource, reqparse
from app.auth.v1.models.user_models import UserModel, Code_problemsModel, Search_code_problem,language, code_problem

user_model_view = UserModel()
codeproblem_model_view = Code_problemsModel()
get_codeproblem_model_view = code_problem()
search_model_view=Search_code_problem()
language_model_view=language()

class UserRegister(Resource):
    """
    User class view for register endpoint
    """

    parser = reqparse.RequestParser()
    parser.add_argument("email", type=str, required=True, help="Please input an email")
    parser.add_argument("username", type=str, required=True, help="Please input your name")

    def post(self):
        """
        HTTP method to register a new user
        """
        try:
            args = UserRegister.parser.parse_args()
            args = request.get_json()
            new_user = user_model_view.create_user(
                username=args['username'],
                email=args['email'],
                password=args['password'],
                confirm_password=args['confirm_password']
                )


        except Exception as e:
            return {
                "status": 400,
                "error": "Invalid Key error {}".format(e)
            }, 400

        return {
            "status": 201,
            "data": new_user
        }, 201

class Code_problemsModel(Resource):
    '''
    This is a class for code problems end point
    '''
    parser = reqparse.RequestParser()
    parser.add_argument("title", type=str, required=True, help="Please input the title")
    parser.add_argument("language", type=str, required=True, help="Please input the language of your coding problem")
    parser.add_argument("content",type=str, required=True, help= "Please Enter your coding problem")

    def post(self):
        '''
        HTTP request to create a Coding Problem
        '''
        try:
            args=Code_problemsModel.parser.parse_args()
            args = request.get_json()
            new_codep = codeproblem_model_view.create_codep(
                    
                    title=args['title'],
                    language=args['language'],
                    content=args['content'],
                    
                )
        except Exception as e:
            return {
                    "status": 400,
                    "error": "Invalid Key error {}".format(e)
                }, 400

        return {
            "status": 201,
            "data": new_codep
        }, 201

class code_problem(Resource):

    def get(self,title):
        data=get_codeproblem_model_view.get_codep_by_title(title)

        return{
            "status":200,
            "data": data
        },200

class Search_code_problem(Resource):

    def get(self,codeId):
        # codeId=str(codeId)
        data=search_model_view.get_codep_by_codeId(codeId)
        return {
            "status": 201,
            "data":data
        },200

class language(Resource):
    def get(self,language):
        language=str(language)
        get_lang=language_model_view.get_codep_by_language(language)
        return{
            "status":200,
            "data":get_lang
        },200

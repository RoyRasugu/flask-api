"""Comment views file"""
from flask_restful import Resource, reqparse
from flask import request, jsonify
from flask_jwt_extended import jwt_required
from app.auth.v1.models.create_problem_models import Code_problemsModel

codeproblem_model_views = Code_problemsModel()

class Code_problemsModel(Resource):
    '''
    This is a class for code problems end point
    '''
    parser = reqparse.RequestParser()
    parser.add_argument("title", type=str, required=True, help="Please input the title")
    parser.add_argument("language", type=str, required=True, help="Please input the language of your coding problem")
    parser.add_argument("content",type=str, required=True, help= "Please Enter your coding problem")

    @jwt_required
    def post(self):
        '''
        HTTP request to create a Coding Problem
        '''
     
        args=Code_problemsModel.parser.parse_args()
        args = request.get_json()
        # import pdb; pdb.set_trace()
        new_codep = codeproblem_model_views.create_codep(
                
                title=args['title'],
                language=args['language'],
                content=args['content']
                )

        return {
            "status": 201,
            "data": new_codep
        }, 201

"""searchproblem views file"""
from flask_restful import Resource, reqparse
from flask import request, jsonify
from flask_jwt_extended import jwt_required
from app.auth.v1.models.search_problem_models import Search_code_problemModel

search_views = Search_code_problemModel()

class Search_code_problem(Resource):
    @jwt_required
    def get(self,codeId):
        codeId=str(codeId)
        data=search_views.get_codep_by_codeId(codeId)
        return {
            "status": 201,
            "data":data
        },200

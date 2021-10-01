"""Language views file"""
from flask_restful import Resource, reqparse
from flask import request, jsonify
from flask_jwt_extended import jwt_required
from app.auth.v1.models.langage_models import languageModel

language_views = languageModel()

class LanguageViewsResource(Resource):
    @jwt_required
    def get(self,language):
        language=str(language)
        get_lang=language_views.get_codep_by_language(language)
        return{
            "status":201,
            "data":get_lang
        },201
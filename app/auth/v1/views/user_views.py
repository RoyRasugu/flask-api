from flask import request
from flask_restful import Resource, reqparse
from app.auth.v1.models.user_models import UserModels
from app.auth.v1.models.user_models import Comment

user_model_view = UserModels()

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

class

from flask import request
from flask_restful import Resource, reqparse
from app.auth.v1.models.user_models import UserModels


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

class UserLogin(Resource):
    """
    User class view to login a user
    """
    parser = reqparse.RequestParser()
    parser.add_argument("email", type=str, required=True, help="PLease input an email")
    parser.add_argument("password", type=str, required=True, help="Please input your password")

    def post(self):
        """
        HTTP method to login a user
        """
        try:
            args = UserLogin.parser.parse_args()
            email = args.get('email')
            password = args.get('password')
        
        except Exception as e:
            return {
                "status": 400,
                "error": "Invalid Key error. You should provide an email and password"
            }, 400

        user_email_exists = user_model_view.get_user_by_email(email)
        # it will return the user info

        if not user_email_exists:
            return {
                "status": 404,
                "error": "You need a valid email address to login"
            }, 404

        check_user_password = user_model_view.validate_password(email,password)

        if not check_user_password:
            return {
                "status": 404,
                "error": "Invalid password. Please provide the correct password"
            }, 400

        for data in user_email_exists:
            response = {
                "id": user_email_exists["userid"],
                "email": user_email_exists["email"],
            }

        return {
            "status": 201, 
            "data": response
        }, 201


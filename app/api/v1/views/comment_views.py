"""Comment views file"""
from flask_restful import Resource, reqparse
from flask import request, jsonify
from flask_jwt_extended import jwt_required
from app.auth.v1.models.comment_models import CommentsModel

comment_views = CommentsModel()


class CommentViewsResource(Resource):
    """Comments class for posting comments"""

    parser = reqparse.RequestParser()
    parser.add_argument("body", type=str, required=True, help="Please input your comment")

    @jwt_required
    def post(self):
        """
        HTTP method to post a new comment
        """
        
        args=CommentViewsResource.parser.parse_args()
        args = request.get_json()
        body = args['body']
        new_comment = comment_views.create_comment(body)

        return {
            "status": 201,
            "data": new_comment,
            "Message": "Comment successfully created"
        }, 201
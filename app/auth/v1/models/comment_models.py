"""Comment CRUD functionality"""
from app.auth.v1.models.db_model import Quora_Db

class CommentsModel:
    '''
    A class to add user comments to code problems
    '''

    def create_comment(self, body):
        '''
        Method to create user comments
        '''

        comment_querry = """
        INSERT INTO Comments( body)
        VALUES(%s)
        RETURNING comments_Id,body
        """

        comment_data = (body,)

        response = Quora_Db.add_to_db(comment_querry, comment_data)
        return response
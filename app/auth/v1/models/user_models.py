from .import db
from .db_model import Quora_Db
from datetime import datetime
class UserModels():
    """
    Class for the user operations
    """
    
    def create_user(self, username, email, password, confirm_password):
        """
        Method to create a new user record
        """
        email_query = """SELECT * FROM users WHERE email = '{}'""".format(email)
        duplicate_email = Quora_Db.retrieve_all(email_query)
        if duplicate_email:
            return False

        user_query = """
        INSERT INTO users (username, email, password, confirm_password)
        VALUES(%s, %s, %s, %s)
        RETURNING email, username
        """
        user_data = (username, email, password, confirm_password)

        response = Quora_Db.add_to_db(user_query, user_data)
        return response

    def get_user_by_email(self, email):
        """Get user by email"""
        user_email_query = """SELECT * FROM users WHERE email = '{}'""".format(
            email)
        user_response = Quora_Db.retrieve_one(user_email_query)
        if not user_response:
            return False
        return user_response

class Comment(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    comment = db.Column(db.String)
    posted = db.Column(db.DateTime, default=datetime.utcnow)
    code_problems_id = db.Column(db.Integer, db.ForeignKey('problem.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.remove(self)
        db.session.commit()

    def get_comment(id):
        comment = Comment.query.all(id.id)
        return comment

    @classmethod
    def get_comments(cls,id):
        comments = Comment.query.filter_by(code_problems_id=id).all()
        return comments

    def __repr__(self):
        return f"Comment : id: {self.id} comment: {self.comment}"

    


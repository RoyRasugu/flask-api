from .db_model import Quora_Db

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

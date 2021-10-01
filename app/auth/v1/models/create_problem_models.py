"""CreatecodeProblem CRUD functionality"""
from app.auth.v1.models.db_model import Quora_Db

class Code_problemsModel:
    '''
    This class creates a code problems operations
    '''
    def create_codep(self, title, language, content):
        '''
        Method to create a coding problem
        '''
        
        codep_querry = """
        INSERT INTO code_problems(title, language, content)
        VALUES(%s, %s, %s)
        RETURNING codeId, title, language, content
        """

        codep_data = (title, language, content)

        response = Quora_Db.add_to_db(codep_querry, codep_data)
        return response

    def get_codep_by_title(self, title):
        '''
        Get coding problem by its title
        '''
        codep_title_querry='''SELECT * FROM code_problems WHERE title = {}'''.format(title)
        codep_response = Quora_Db.retrieve_all(codep_title_querry)
        if not codep_response:
            return False
        return codep_response
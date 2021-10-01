"""language CRUD functionality"""
from app.auth.v1.models.db_model import Quora_Db

class languageModel:
   
    def get_codep_by_language(self, language):
        ''' A class to search by language'''

        codep_language_querry = '''SELECT * FROM code_problems WHERE language = '{}' '''.format(language)
        codep_response = Quora_Db.retrieve_all(codep_language_querry)
        if not codep_response:
            return False
        return codep_response
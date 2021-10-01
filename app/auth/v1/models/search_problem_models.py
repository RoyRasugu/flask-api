"""searchCodeproblem CRUD functionality"""
from app.auth.v1.models.db_model import Quora_Db

class Search_code_problemModel:
    def get_codep_by_codeId(self, codeId):
        '''
        Get coding problem by its code Id
        '''
        # codeId=
        codep_codeId_querry='''SELECT * FROM code_problems WHERE codeId = {}'''.format(codeId)
        codep_response = Quora_Db.retrieve_all(codep_codeId_querry)
        if not codep_response:
            return False
        return codep_response
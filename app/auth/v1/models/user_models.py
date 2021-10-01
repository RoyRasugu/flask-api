       
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

        response = myapi.add_to_db(codep_querry, codep_data)
        return response

    def get_codep_by_title(self, title):
        '''
        Get coding problem by its title
        '''
        codep_title_querry='''SELECT * FROM code_problems WHERE title = {}'''.format(title)
        codep_response = myapi.retrieve_all(codep_title_querry)
        if not codep_response:
            return False
        return codep_response

class Search_code_problem:
    def get_codep_by_codeId(self, codeId):
        '''
        Get coding problem by its code Id
        '''
        # codeId=
        codep_codeId_querry='''SELECT * FROM code_problems WHERE codeId = {}'''.format(codeId)
        codep_response = myapi.retrieve_all(codep_codeId_querry)
        if not codep_response:
            return False
        return codep_response

class language:
   
    def get_codep_by_language(self, language):
        ''' A class to search by language'''

        codep_language_querry = '''SELECT * FROM code_problems WHERE language = '{}' '''.format(language)
        codep_response = myapi.retrieve_all(codep_language_querry)
        if not codep_response:
            return False
        return codep_response

class Comments:
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

        response = api.add_to_db(comment_querry, comment_data)
        return response
   

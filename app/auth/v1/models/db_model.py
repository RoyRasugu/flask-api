

    @classmethod
    def build_tables(cls):
        """
        Method to create the tables in the database
        """
        try:
            
            cls.cur.execute("""
            CREATE TABLE IF NOT EXISTS code_problems(
                codeId serial PRIMARY kEY,
                title VARCHAR NOT NULL,
                language VARCHAR NOT NULL,
                content VARCHAR NOT NULL
            )
            """)
            cls.cur.execute("""
            CREATE TABLE IF NOT EXISTS comments(
                comments_Id serial PRIMARY kEY,
                body VARCHAR NOT NULL,
                CONSTRAINT fk_code_problem
                FOREIGN KEY(codeId)
                REFERENCES code_problems(codeId)
            )
            """)

            cls.conn.commit()
            print('Tables successfully created')
        except Exception as e:
            Error(e)
            print('What happened? =>', e)

    @classmethod
    def remove_row(cls, query_string):
        cls.cur.execute(query_string)
        return cls.cur.remove_row()


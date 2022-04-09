import psycopg2
import logging


class PostgreDbOperations:
    def __init__(self, database:str, user:str,
                 password:str, host:str, port:str, autocommit:bool):
        self.database = database
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.autocommit = autocommit

    def connect(self):
        try:
            self.connection = psycopg2.connect(dbname=self.database,
                                            user=self.user,
                                            password=self.password,
                                            host=self.host,
                                            port=self.port)
        except (psycopg2.OperationalError,AttributeError):
            print("CHECK THE CONNECTION ATTRIBUTES YOU GIVEN!!!")
        finally:
            self.connection.autocommit = self.autocommit
            self.cursor = self.connection.cursor()

    def search_query(self, query:str,fetchall=False,fetchone=False):
        self.cursor.execute(query)
        if fetchall==True:
            result = self.cursor.fetchall()
            return result
        elif fetchone==True:
            result = self.cursor.fetchone()
            return result
        else:
            print("Check fetch parameter!")
            
    def create_query(self,query:str):
        self.cursor.execute(query)
        return str("Done")
    
    def close(self):
        self.cursor.close()
        self.connection.close()


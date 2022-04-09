import psycopg2
import logging


class PostgreDbOperations:
    def __init__(self, database, user,
                 password, host, port, autocommit):
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
            print("CHECK THE CONNECTION ATTRIBUTES YOU GIVEN!")
        finally:
            self.connection.autocommit = self.autocommit
            self.cursor = self.connection.cursor()

    def query(self, query):
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result

    def close(self):
        self.cursor.close()
        self.connection.close()


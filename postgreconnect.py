import psycopg2

class PostgreDbOperations:
    def __init__(self,database,user,
                 password,host,port,autocommit):
        self.database=database
        self.user=user
        self.password=password
        self.host=host
        self.port=port
        self.autocommit=True
        
    def connect(self):
        self.connection = psycopg2.connect(dbname=self.database,
                                           user=self.user,password=self.password,
                                           host=self.host,port=self.port)
        
        self.connection.autocommit = self.autocommit
        self.cursor = self.connection.cursor()

        
    def query(self,query):
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result
            
    def close(self):
            self.cursor.close()
            self.connection.close()
    


db_connect = PostgreDbOperations("ibb_ulasim",'postgres','44410','127.0.0.1','5432',True)
db_connect.connect()
print(db_connect.query("SELECT * ;"))
db_connect.close()




# def connect_db():
#     """:return: returns conn"""
#     try:
#         conn = psycopg2.connect(
#             database="ibb_ulasim",
#             user='postgres',
#             password='44410',
#             host='127.0.0.1',
#             port='5432')
#         conn.autocommit = True
#         return conn
#     except:
#         print("Cannot connect to db")
        



# import psycopg2

# class DatabaseOperations:
#     def __init__(self,database,user,
#                  password,host,port,autocommit):
#         self.database=database,
#         self.user=user,
#         self.password=password,
#         self.host=host,
#         self.port=port,
#         self.autocommit=True
        
    
#     def connect(self):
#         self.connection = psycopg2.connect(f"dbname={str(self.database)[1:-2]} user={str(self.user)[1:-2]} password={str(self.password)[1:-2]} host={str(self.host)[1:-2]}" )
#         self.connection.autocommit = self.autocommit
#         self.cursor = self.connection.cursor()

        
#     def query(self,query):
#         self.cursor.execute(query)
#         a = self.cursor.fetchall()
#         return a
            
#     def close(self):
#             self.cursor.close()
#             self.connection.close()

        
        
# db_connect = DatabaseOperations("ibb_ulasim",'postgres','44410','127.0.0.1','5432',True)
# db_connect.connect()
# print(db_connect.query("SELECT * FROM ulasim ;"))





# # def connect_db():
# #     """:return: returns conn"""
# #     try:
# #         conn = psycopg2.connect(
# #             database="ibb_ulasim",
# #             user='postgres',
# #             password='44410',
# #             host='127.0.0.1',
# #             port='5432')
# #         conn.autocommit = True
# #         return conn
# #     except:
# #         print("Cannot connect to db")
        

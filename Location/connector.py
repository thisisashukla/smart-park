'''
Created on 19 Dec 2016

@author: Ankur
'''

import psycopg2

class postgresConnector:
    
    def __init__(self,dbname):
        self.db_host = "localhost"
        self.db_user = "postgres"
        self.db_passwd = ""
        self.db_database = dbname
        self.db_port = "5432"
        
    
    def getCursor(self):
        
        # connect to DB
        conn = psycopg2.connect(host=self.db_host, user=self.db_user, port=self.db_port, password=self.db_passwd, database=self.db_database)
        # create a cursor
        cur = conn.cursor()
        return conn,cur
        
    def closeConnection(self,conn,cur):
        # clean up and close database curson and connection
        cur.close()
        
        conn.close()

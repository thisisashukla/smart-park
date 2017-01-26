'''
Created on 09-Jan-2017

@author: MDSharma
'''
import os
import psycopg2
import urlparse

class postgresConnector:

    def __init__(self,dbname):
        self.db_host = "localhost"
        self.db_user = "postgres"
        self.db_passwd = "postgres"
        self.db_database = dbname
        self.db_port = "5432"


    def getConnCur(self):
        # connect to DB
        urlparse.uses_netloc.append("postgres")
        url = urlparse.urlparse(os.environ["DATABASE_URL"])

        conn = psycopg2.connect(database=url.path[1:],user=url.username,password=url.password,host=url.hostname,port=url.port)
        # create a cursor
        cur = conn.cursor()
        return conn,cur

    def closeConnection(self,conn,cur):
        # clean up and close database curson and connection
        cur.close()

        conn.close()

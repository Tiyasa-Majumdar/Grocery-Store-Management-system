'''import mysql.connector
__cnx = None

def get_sql_connection():
    global __cnx
    if __cnx is None:
        __cnx = mysql.connector.connect(user='root', password='Tiyasa',
                              host='127.0.0.1',
                              database='gs',
                              autocommit=True) 
    return __cnx '''

import os
import mysql.connector

def get_sql_connection():
    return mysql.connector.connect(
        host=os.environ.get("grocery-mysql-grocery-management1.j.aivencloud.com"),
        port=int(os.environ.get("DB_PORT", 17369)),
        user=os.environ.get("avnadmin"),
        password=os.environ.get("AVNS_51Jkk8UDs4_gutxZFMm"),
        database=os.environ.get("defaultdb"),
        autocommit=True
    )

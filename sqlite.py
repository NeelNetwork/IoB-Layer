import sqlite3 
from sqlite3 import Error
def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        print 
        return conn
    except Error as e:
        print(e)
    return None
# cursor = conn.cursor()
def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def create_keypair(conn , keys):

    sql = """ INSERT INTO keys(waves_address , bitcoin_address , bitcoin_privatekey)
    VALUES(?,?,?)"""
    cur = conn.cursor()
    cur.execute(sql, keys)
    return cur.lastrowid


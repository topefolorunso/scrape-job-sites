import sqlite3

from sqlalchemy import create_engine



def get_database():
    conn = create_engine('sqlite:///database/jobs.db')

def connect_to_database():
    try:
        conn = sqlite3.connect('database/jobs.db')
        print('Database connection iniialized')

    except sqlite3.Error as error:
        conn = None
        print('Error occurred: ', error)

    return conn


def query_database(conn, type, query=None):
    try:
        cursor = conn.cursor()
        cursor.execute(query)

        if type in ('insert', 'update'):
            conn.commit()

        else:
            result = cursor.fetchall()
            return result
    
    except Exception as error:
        if conn:
            conn.close()
            print('Database connection closed')
        raise error  

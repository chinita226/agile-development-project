"""Module for database actions."""
import sqlite3
from sqlite3 import Error
 
 
def create_database(db_path):
    """Create an SQLite database."""
    connection = None
    try:
        connection = sqlite3.connect(db_path)
 
    except Error as e:
        print(e)
 
    finally:
        if connection:
            connection.close()
 
 
def query(sql):
    """Get data from database."""
    with sqlite3.connect('database.db') as con:
        try:
            cur = con.cursor()
            cur.execute(sql)
            res = cur.fetchall()
        except Error as e:
            print(e)
 
    return res
 
 
def update(sql):
    """Maniulate data in the database."""
    with sqlite3.connect('database.db') as con:
        try:
            cur = con.cursor()
            cur.execute(sql)
            con.commit()
        except Error as e:
            print(e)

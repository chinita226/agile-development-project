import sqlite3
from sqlite3 import Error


def create_database(db_name):
    """Create an SQLite database."""
    connection = None
    try:
        connection = sqlite3.connect(db_name)

    except Error as e:
        print(e)

    finally:
        if connection:
            connection.close()


if __name__ == "__main__":
    create_database("../database.db")

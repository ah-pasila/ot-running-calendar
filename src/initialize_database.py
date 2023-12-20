from database_connection import get_database_connection

"""Class for initializing SQL database including removing old tables (if any) 
    and setting up new tables for users and plans 
"""


def _drop_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        DROP table IF EXISTS users;          
    ''')

    cursor.execute('''
        DROP table IF EXISTS plans;          
    ''')

    connection.commit()


def _create_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            gender TEXT,
            age INTEGER
        );
    ''')

    cursor.execute('''
        CREATE TABLE plans (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            day TEXT NOT NULL,
            type TEXT NOT NULL,
            duration INTEGER,
            length INTEGER,
            description TEXT,
            username TEXT
        );
    ''')


def initialize_database():
    connection = get_database_connection()
    _drop_tables(connection)
    _create_tables(connection)


if __name__ == "__main__":
    initialize_database()
    print("Database intitialized")

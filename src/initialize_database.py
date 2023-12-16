from database_connection import get_database_connection

"""Class for initializing database including removing tables and setting up new tables
"""


def drop_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        drop table if exists users;          
    ''')

    cursor.execute('''
        drop table if exists plans;          
    ''')

    connection.commit()



def create_tables(connection):
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
            type INT NOT NULL,
            duration INT NOT NULL,
            length INTEGER,
            username TEXT
        );
    ''')


def initialize_database():
    connection = get_database_connection()
    drop_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()
    print("Database intitialized")

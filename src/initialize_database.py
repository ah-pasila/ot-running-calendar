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
        create table users (
            username text primary key,
            password text,
            gender text,
            age int
        );
    ''')

    cursor.execute('''
        create table plans (
            day text primary key,
            description text,
            length int,
            username text
        );
    ''')


def initialize_database():
    connection = get_database_connection()
    drop_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()
    print("Database intitialized")

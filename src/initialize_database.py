from database_connection import get_database_connection

#Taulujen poisto

def drop_tables(connection):
    cursor = connection.cursor()
    
    cursor.execute('''
        drop table if exists users;
        drop table if exists plans;            
    ''')

    connection.commit()

#Taulujen luonti

def create_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        create table users (
            username text primary key,
            password text,
            gender text,
            age int
        );
        create table plans (
            day text primary key,
            description text,
            length int,
            username text REFERENCES users(username)
        );
    ''')

#Taulujen alustus eli poisto ja luonti

def initialize_database():
    connection = get_database_connection()
    drop_tables(connection)
    create_tables(connection)
    
if __name__ == "__main__":
    initialize_database()
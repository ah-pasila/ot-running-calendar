import os
import sqlite3

"""database_connection.py is used to create connection to the local DB

    Returns:
        connection: returns DB connection
"""

dirname = os.path.dirname(__file__)

connection = sqlite3.connect(os.path.join(
    dirname, "..", "data", "database.sqlite"))
connection.row_factory = sqlite3.Row


def get_database_connection():
    return connection

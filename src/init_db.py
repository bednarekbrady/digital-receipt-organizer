import sqlite3
import os

# Create database in the parent directory (project root)
db_path = os.path.join(os.path.dirname(__file__), '..', 'database.db')

connection = sqlite3.connect(db_path)

with open(os.path.join(os.path.dirname(__file__), 'schema.sql')) as f:
    connection.executescript(f.read())

connection.commit()
connection.close()
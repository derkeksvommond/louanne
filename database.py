import sqlite3

connection = sqlite3.connect("database.db")
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE test IF NOT EXISTS ()
""")

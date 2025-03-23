import sqlite3
import os

db_path = 'user_data.db'

if os.path.exists(db_path):
    os.remove(db_path)
    print("Database deleted.")

conn = sqlite3.connect(db_path)
c = conn.cursor()

c.execute('''
    CREATE TABLE IF NOT EXISTS user_data (
        id INTEGER UNIQUE PRIMARY KEY AUTOINCREMENT,
        email TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        admin INTEGER DEFAULT 0 
    )
''')

conn.commit()
conn.close()

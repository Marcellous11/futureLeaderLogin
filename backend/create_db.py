import sqlite3
import os

db_path = 'user_data.db'

if os.path.exists(db_path):
    os.remove(db_path)
    print("Database deleted.")

# Connect to SQLite database
conn = sqlite3.connect(db_path)
c = conn.cursor()

# Create a table to store emails and passwords
c.execute('''
    CREATE TABLE IF NOT EXISTS user_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT NOT NULL,
        password TEXT NOT NULL
    )
''')

# Sample data: emails and corresponding passwords
user_data = [
    ('john.doe@example.com', 'mysecretpassword'),
    ('jane.smith@example.com', 'anotherpassword')
]

# Insert data into user_data table
c.executemany('''
    INSERT INTO user_data (email, password) VALUES (?, ?)
''', user_data)

# Commit changes and close connection
conn.commit()
conn.close()

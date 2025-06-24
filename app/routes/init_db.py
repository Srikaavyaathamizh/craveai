import sqlite3
import os

# Go up two levels and into data/
db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'sarab_ai.db'))

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS owners (
    ownername TEXT PRIMARY KEY,
    password TEXT
)
''')

conn.commit()
conn.close()
print("✅ 'owners' table created successfully.")

import sqlite3

DB_FILE = "test_db.db"

# Create or reset the test_db database
with sqlite3.connect(DB_FILE) as conn:
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS users")
    cursor.execute("""
        CREATE TABLE users (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER NOT NULL
        )
    """)
    cursor.executemany("INSERT INTO users (name, age) VALUES (?, ?)", [
        ("Alice", 25),
        ("Bob", 42),
        ("Charlie", 39),
        ("Diana", 45),
        ("Eve", 50)
    ])
    conn.commit()

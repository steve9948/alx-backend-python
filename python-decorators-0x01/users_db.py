import sqlite3

def create_users_db():
    conn = sqlite3.connect('users.db')  # Connect to the database
    cursor = conn.cursor()

    # Create the 'users' table if it doesn't exist
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL
    )
    ''')

    # Insert sample data
    cursor.execute("INSERT INTO users (name, email) VALUES ('John Doe', 'john@example.com')")
    cursor.execute("INSERT INTO users (name, email) VALUES ('Jane Smith', 'jane@example.com')")

    # Commit changes and close the connection
    conn.commit()
    conn.close()

# Call the function to create the database and set up the table
create_users_db()
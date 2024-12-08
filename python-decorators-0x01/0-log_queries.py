import sqlite3
import functools
from datetime import datetime

# Decorator to log SQL queries with timestamp
def log_queries(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        query = kwargs.get('query') or (args[0] if args else None)
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if query:
            print(f"[{timestamp}] Executing SQL Query: {query}")
        else:
            print(f"[{timestamp}] No SQL query provided.")
        return func(*args, **kwargs)
    return wrapper

@log_queries
def fetch_all_users(query):
    conn = sqlite3.connect('users.db')  # Open the database connection
    cursor = conn.cursor()
    cursor.execute(query)  # Execute the query
    results = cursor.fetchall()  # Fetch all results
    conn.close()  # Close the connection
    return results

# Fetch users while logging the query
users = fetch_all_users(query="SELECT * FROM users")
print(users)

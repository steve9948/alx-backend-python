import sqlite3
import functools

#### decorator to lof SQL queries

""" YOUR CODE GOES HERE"""
def log_queries():
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Assuming the first argument is the query
            query = kwargs.get('query') or (args[0] if args else None)
            if query:
                print(f"Executing SQL Query: {query}")
            else:
                print("No SQL query provided.")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@log_queries
def fetch_all_users(query):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

#### fetch users while logging the query
users = fetch_all_users(query="SELECT * FROM users")
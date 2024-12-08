import sqlite3
import functools

query_cache = {}

# Decorator to automatically handle database connections
def with_db_connection(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect('users.db')  # Open the database connection
        try:
            result = func(conn, *args, **kwargs)  # Pass the connection to the wrapped function
        finally:
            conn.close()  # Ensure the connection is closed
        return result
    return wrapper

# Decorator to cache query results
def cache_query(func):
    @functools.wraps(func)
    def wrapper(conn, query):
        if query in query_cache:
            print("Using cached result for query:", query)
            return query_cache[query]
        else:
            print("Executing query and caching result:", query)
            result = func(conn, query)
            query_cache[query] = result
            return result
    return wrapper

@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

# First call will cache the result
users = fetch_users_with_cache(query="SELECT * FROM users")

# Second call will use the cached result
users_again = fetch_users_with_cache(query="SELECT * FROM users")

print(users)
print(users_again)

import sqlite3
import functools
import time

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

# Decorator to retry a function upon transient failure
def retry_on_failure(retries=3, delay=2):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempt = 0
            while attempt < retries:
                try:
                    return func(*args, **kwargs)
                except (sqlite3.OperationalError, sqlite3.ProgrammingError) as e:
                    attempt += 1
                    print(f"Attempt {attempt} failed: {e}. Retrying in {delay} seconds...")
                    time.sleep(delay)
            raise Exception(f"Function '{func.__name__}' failed after {retries} attempts.")
        return wrapper
    return decorator

@with_db_connection
@retry_on_failure(retries=3, delay=1)
def fetch_users_with_retry(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()

# Attempt to fetch users with automatic retry on failure
users = fetch_users_with_retry()
print(users)
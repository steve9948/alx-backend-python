import mysql.connector
from mysql.connector import Error

class DatabaseConnection:
    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.connection = None

    def __enter__(self):
        try:
            # Establish the connection
            self.connection = mysql.connector.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            if self.connection.is_connected():
                print("Connected to the database")
                return self.connection  # Return the connection for use within 'with' block
        except Error as e:
            print(f"Error: {e}")
            raise

    def __exit__(self, exc_type, exc_value, traceback):
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("Database connection closed")
        # Handle exceptions, if any
        if exc_type:
            print(f"Exception occurred: {exc_value}")
        return False  # Propagate exceptions if any occur

# Usage example
if __name__ == "__main__":
    # Database credentials
    db_config = {
        "host": "localhost",
        "database": "test_db",
        "user": "steve",
        "password": "root"
    }

    # Using the custom context manager
    with DatabaseConnection(**db_config) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        results = cursor.fetchall()
        for row in results:
            print(row)

import mysql.connector
from mysql.connector import Error

class ExecuteQuery:
    def __init__(self, db_config, query, params=None):
        """
        Initialize with database configuration, query, and optional parameters.
        """
        self.db_config = db_config
        self.query = query
        self.params = params
        self.connection = None
        self.cursor = None

    def __enter__(self):
        """
        Open the database connection and execute the query.
        """
        try:
            # Establish the connection
            self.connection = mysql.connector.connect(**self.db_config)
            if self.connection.is_connected():
                print("Connected to the database")
                self.cursor = self.connection.cursor()
                self.cursor.execute(self.query, self.params)
                return self.cursor  # Return the cursor for fetching results
        except Error as e:
            print(f"Error: {e}")
            raise

    def __exit__(self, exc_type, exc_value, traceback):
        """
        Close the cursor and the connection.
        """
        if self.cursor:
            self.cursor.close()
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("Database connection closed")
        # Handle exceptions
        if exc_type:
            print(f"Exception occurred: {exc_value}")
        return False  # Propagate exceptions if any

# Usage example
if __name__ == "__main__":
    # Database configuration
    db_config = {
        "host": "localhost",
        "database": "test_db",
        "user": "your_username",
        "password": "your_password"
    }

    # Query and parameters
    query = "SELECT * FROM users WHERE age > %s"
    params = (25,)  # Parameter for the query

    # Using the context manager to execute the query
    with ExecuteQuery(db_config, query, params) as cursor:
        results = cursor.fetchall()
        for row in results:
            print(row)

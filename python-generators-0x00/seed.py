import mysql.connector
import csv
from uuid import uuid4

def connect_db():
    """
    Connects to the MySQL database server.
    Returns a connection object if successful, or None if not.
    """
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='steve',
            password='root'
        )
        print("Connected to MySQL server.")
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def create_database(connection):
    """
    Creates the ALX_prodev database if it doesn't exist.
    """
    cursor = connection.cursor()
    try:
        cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
        print("Database ALX_prodev created or already exists.")
    except mysql.connector.Error as err:
        print(f"Error creating database: {err}")
    finally:
        cursor.close()

def connect_to_prodev():
    """
    Connects to the ALX_prodev database.
    """
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='steve',
            password='root',
            database='ALX_prodev'
        )
        print("Successfully connected to ALX_prodev.")
        return connection
    except mysql.connector.Error as err:
        print(f"Error connecting to ALX_prodev: {err}")
        return None

def create_table(connection):
    """
    Creates the user_data table if it doesn't exist.
    """
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_data (
            user_id CHAR(36) PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            age DECIMAL(3, 0) NOT NULL
        )
    """)
    print("Table 'user_data' created or already exists.")
    cursor.close()

def insert_data(connection, file_path):
    """
    Inserts data into the user_data table from a CSV file.
    """
    cursor = connection.cursor()
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip header
        for row in csv_reader:
            user_id = str(uuid4())
            name, email, age = row
            cursor.execute("""
                INSERT INTO user_data (user_id, name, email, age) 
                VALUES (%s, %s, %s, %s)
                ON DUPLICATE KEY UPDATE name=VALUES(name), email=VALUES(email), age=VALUES(age)
            """, (user_id, name, email, age))
    connection.commit()
    cursor.close()
    print(f"Data inserted into 'user_data' table.")

def stream_rows(connection):
    """
    Streams rows from the user_data table using a generator.
    """
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM user_data")
    for row in cursor.fetchall():
        yield row
    cursor.close()

if __name__ == '__main__':
    # Step 1: Connect to MySQL server
    server_connection = connect_db()
    if server_connection:
        create_database(server_connection)
        server_connection.close()

    # Step 2: Connect to ALX_prodev database
    db_connection = connect_to_prodev()
    if db_connection:
        create_table(db_connection)
        insert_data(db_connection, 'user_data.csv')

        # Streaming data
        print("Streaming rows:")
        for row in stream_rows(db_connection):
            print(row)

        db_connection.close()

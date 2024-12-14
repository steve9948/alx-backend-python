import mysql.connector

def connect_to_prodev():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='steve',
            password='root',
            database='ALX_prodev'
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def stream_users():
    connection = connect_to_prodev()
    if not connection:
        print("Error connecting to the database.")
        return

    cursor = connection.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM user_data")
        for row in cursor:
            yield row
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        connection.close()

# Make `stream_users` accessible as a callable attribute of the module
if __name__ == "__main__":
    for user in stream_users():
        print(user)
else:
    stream_users = stream_users  # Ensure the function is correctly exposed

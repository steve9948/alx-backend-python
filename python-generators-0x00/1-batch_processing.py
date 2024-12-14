import mysql.connector

def connect_to_prodev():
    """Establish connection to the database."""
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

def stream_users_in_batches(batch_size):
    """Fetch rows in batches from the database."""
    connection = connect_to_prodev()
    if not connection:
        print("Error connecting to the database.")
        return

    cursor = connection.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM user_data")
        while True:
            batch = cursor.fetchmany(batch_size)
            if not batch:
                break
            yield batch
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        connection.close()

def batch_processing(batch_size):
    """Process each batch to filter users over the age of 25."""
    for batch in stream_users_in_batches(batch_size):
        processed_users = [
            user for user in batch if user['age'] > 25
        ]
        for user in processed_users:
            print(user)

#!/usr/bin/python3
import mysql.connector
from seed import connect_to_prodev


def stream_user_ages():
    """
    Generator that streams user ages one by one from the user_data table.
    """
    connection = connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    
    try:
        cursor.execute("SELECT age FROM user_data")
        for row in cursor:
            print("Yielding age:", row['age'])  # Debug print
            yield row['age']
    finally:
        cursor.close()
        connection.close()


def calculate_average_age():
    """
    Calculate the average age of users using the stream_user_ages generator.
    """
    total_age = 0
    count = 0

    for age in stream_user_ages():
        total_age += age
        count += 1

    if count == 0:
        print("No users found.")
    else:
        average_age = total_age / count
        print(f"Average age of users: {average_age:.2f}")

if __name__ == "__main__":
    calculate_average_age()

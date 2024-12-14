seed = __import__('seed')

def paginate_users(page_size, offset):
    """Fetch rows from the database using LIMIT and OFFSET."""
    connection = seed.connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute(f"SELECT * FROM user_data LIMIT {page_size} OFFSET {offset}")
    rows = cursor.fetchall()
    connection.close()
    return rows

def lazy_paginate(page_size):
    """Generator function to lazily fetch paginated data."""
    offset = 0
    while True:
        page = paginate_users(page_size, offset)
        if not page:  # Stop when there are no more rows
            break
        yield page
        offset += page_size

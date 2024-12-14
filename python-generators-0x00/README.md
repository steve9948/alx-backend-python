# Python Generators - Task Overview

This repository contains solutions to tasks aimed at mastering Python generators for memory-efficient and lazy data processing. Below is a breakdown of all tasks, their objectives, and implementation details.

## Tasks

### Task 0: Streaming Rows from a SQL Database

**Objective:**

Create a generator function that streams rows from a SQL database one by one.

**Implementation:**

Write a function `stream_users()` in `0-stream_users.py`:

* Fetch rows from the `user_data` table using a generator.
* Use a single loop to yield rows.

**Usage:**

Tested using the `1-main.py` script:

```python
from itertools import islice
stream_users = __import__('0-stream_users')

for user in islice(stream_users(), 6):
    print(user)
Task 1: Batch Processing with Generators
Objective:

Fetch rows in batches and process each batch to filter users over the age of 25.

Implementation:

stream_users_in_batches(batch_size): Fetches rows in batches from the database.
batch_processing(batch_size): Processes each batch to filter users older than 25.
Prototype:

Python

def stream_users_in_batches(batch_size):
    ...

def batch_processing(batch_size):
    ...
Usage:

Tested using 2-main.py:

Python

import sys
processing = __import__('1-batch_processing')

processing.batch_processing(50)
Task 2: Lazy Pagination with Generators
Objective:

Simulate fetching paginated data from the user_data table using a generator to load each page lazily.

Implementation:

paginate_users(page_size, offset): Fetches a specific page of data.
lazy_paginate(page_size): Uses paginate_users to fetch pages lazily as needed.
Prototype:

Python

def paginate_users(page_size, offset):
    ...

def lazy_paginate(page_size):
    ...
Usage:

Tested using 3-main.py:

Python

lazy_paginator = __import__('2-lazy_paginate').lazy_pagination

for page in lazy_paginator(100):
    for user in page:
        print(user)
Task 3: Memory-Efficient Average Calculation
Objective:

Use a generator to calculate the average age of users in a large dataset without loading the entire dataset into memory.

Implementation:

stream_user_ages(): Yields user ages one by one.
calculate_average_age(): Uses the generator to compute the average age.
Prototype:

Python

def stream_user_ages():
    ...

def calculate_average_age():
    ...
Usage:

Executed directly:

Bash

python 4-stream_ages.py
Expected Output:

Bash

Average age of users: <average_age>
General Instructions
Ensure the user_data table in the database contains valid data.
Database connection is managed via the connect_to_prodev() function from the seed module.
Install necessary dependencies, such as mysql-connector-python.
Example SQL for Populating Data:

SQL

INSERT INTO user_data (name, age, email) VALUES
('Alice', 25, 'alice@example.com'),
('Bob', 30, 'bob@example.com'),
('Charlie', 35, 'charlie@example.com');
Learning Outcomes
Use Python generators for lazy data processing.
Implement batch processing and pagination efficiently.
Perform memory-efficient calculations on large datasets.
Simulate real-world database operations in Python.
Requirements
Python 3.8+
MySQL Database
Dependencies: mysql-connector-python
Repository Structure
.
├── 0-stream_users.py
├── 1-batch_processing.py
├── 2-lazy_paginate.py
├── 3-main.py
├── 4-stream_ages.py
├── seed.py
└── README.md
Author
Steve (ALX Backend Python - Python Generators)
## Data Persistence(L2)

**Step 1: Set Up the MySQL Database**

You need to set up MySQL and create a database and user.

**Step 2: Install Required Python Packages**

Install the required package:

```bash
pip install mysql-connector-python
```

**Step 3: Python Code for Beginners**

```python
import mysql.connector

# Connect to the database
connection = mysql.connector.connect(
    host="localhost",
    user="sampleuser",
    password="samplepass",
    database="sampledb"
)
cursor = connection.cursor()

# Create a table (run this once)
def create_table():
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            age INT
        )
        """
    )

# Add a new user
def insert_user(name, age):
    query = "INSERT INTO users (name, age) VALUES (%s, %s)"
    cursor.execute(query, (name, age))
    connection.commit()

# Fetch and print all users
def list_users():
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    for user in users:
        print(user)

# Main execution
create_table()  # You can run this once and then comment it out
insert_user("John", 20)
insert_user("Jane", 25)
list_users()

# Close the connection
cursor.close()
connection.close()
```

Here's what we've done:

1. Connected to the database at the beginning of the script.
2. Defined three functions:
   - `create_table()`: Creates the `users` table.
   - `insert_user(name, age)`: Adds a user to the database.
   - `list_users()`: Lists all the users in the database.
3. At the end of the script, we call these functions to demonstrate their functionality and then close our connection.

So here The term "data persistence layer" refers to a layer in software architecture responsible for managing data storage and retrieval. In the examples provided, the data persistence layer is represented by the functions and database interactions that handle the storage (insertion) and retrieval of user data from the MySQL database.


1. **Database Connection Initialization**:
    ```python
    connection = mysql.connector.connect(...)
    cursor = connection.cursor()
    ```
   This sets up a connection to the database, which is fundamental to any persistence layer.

2. **Data Creation**:
    ```python
    def create_table():
        ...
    ```

    ```python
    def insert_user(name, age):
        ...
    ```
   The `create_table()` function initializes the table where the data will be stored, ensuring our persistence layer has a place to save user data. The `insert_user()` function persists (or saves) user data into the database.

3. **Data Retrieval**:
    ```python
    def list_users():
        ...
    ```
   The `list_users()` function retrieves and displays user data, showcasing the data retrieval aspect of a persistence layer.


* The data persistence layer in the example is represented by the combined functionality of the three functions (`create_table`, `insert_user`, and `list_users`) and the database connection logic. This layer abstracts away the details of how data is stored and retrieved in the MySQL database, allowing the main application logic to focus on using the data without concerning itself with the specifics of database operations.

In more complex applications, you might have a dedicated class or module for the persistence layer with more advanced features, error handling, caching, etc.
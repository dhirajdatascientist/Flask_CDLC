```python
def create_table():
    conn = sqlite3.connect('infy.db')
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS emp(
                   id INTEGER,
                   username TEXT,
                   email TEXT

    )
""")
    conn.commit()
    conn.close()

```

**Explanation**

1. `import sqlite3`: This line imports a Python library called `sqlite3`, which provides tools for working with SQLite databases.

2. `def create_table():`: This line defines a function named `create_table`. You can call this function to create a table in the SQLite database.

3. `conn = sqlite3.connect('infy.db')`: This line establishes a connection to an SQLite database file named 'infy.db'. If the file doesn't exist, it will be created. The `conn` variable holds this connection.

4. `cursor = conn.cursor()`: This line creates a cursor object. A cursor is like a pointer or a tool used to interact with the database. You can use it to execute SQL commands.

5. `cursor.execute(""" ... """)`: This block of code is where the actual SQL command is executed. The SQL command inside the triple quotes (`"""`) is used to create a table named 'emp' if it doesn't already exist. This table has three columns: 'id' (an integer), 'username' (text), and 'email' (text).

6. `conn.commit()`: After executing the SQL command to create the table, you need to commit the changes to the database. Think of this as saving your changes. This line ensures that any modifications made to the database are finalized.

7. `conn.close()`: Finally, this line closes the connection to the SQLite database. It's essential to close the connection when you're done with it to free up system resources.

**Conclusion**

This code defines a function `create_table` that connects to an SQLite database file, creates a table named 'emp' with three columns if it doesn't exist, saves the changes, and then closes the database connection. This function can be called to set up the 'emp' table in your SQLite database.
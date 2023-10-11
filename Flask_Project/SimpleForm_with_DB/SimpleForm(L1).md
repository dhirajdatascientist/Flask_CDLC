1. First, make sure you have Flask and SQLite3 installed. You can install them using pip if you haven't already:

```
pip install Flask
```

2. Create a new directory for your project, and inside that directory, create a Python file named `app.py`. This file will contain your Flask application.

3. Create an HTML template for your form. Inside the same directory, create a folder named `templates` if it doesn't already exist. Then, inside the `templates` folder, create a file named `index.html`:

`templates/index.html`:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Registration Form</title>
</head>
<body>
    <h1>Registration Form</h1>
    <form method="POST" action="/register">
        <label for="first_name">First Name:</label>
        <input type="text" name="first_name" required><br>

        <label for="password">Password:</label>
        <input type="password" name="password" required><br>

        <input type="submit" value="Register">
    </form>
</body>
</html>
```

4. In your `app.py` file, create a Flask application with a route to render the form and another route to handle form submission and store the data in an SQLite database:

`app.py`:

```python
from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name)

# Define a function to create a database table if it doesn't exist
def create_table():
    conn = sqlite3.connect('user.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Create the table when the app starts
create_table()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    first_name = request.form['first_name']
    password = request.form['password']

    conn = sqlite3.connect('user.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (first_name, password) VALUES (?, ?)", (first_name, password))
    conn.commit()
    conn.close()

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
```

This Flask application creates a simple registration form, stores the first name and password in an SQLite database called `user.db`, and redirects the user to the form page after registration.

5. Run the Flask application:

```
python app.py
```

You can access your application in a web browser at `http://localhost:5000`. Users can enter their first name and password, submit the form, and the data will be stored in the SQLite database.
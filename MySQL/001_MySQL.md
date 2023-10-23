1. **Directory Structure**:

```
/your_project_folder
    /templates
        index.html
        signup.html
    app.py
```

2. **Setup**:

You need to install necessary libraries:

```bash
pip install Flask mysql-connector-python
```

3. **`app.py`**:

```python
from flask import Flask, request, render_template, redirect, url_for
import mysql.connector

app = Flask(__name__)

DATABASE_CONFIG = {
    'host': 'your_host',
    'user': 'your_username',
    'password': 'your_password',
    'database': 'your_database'
}

@app.route('/')
def index():
    return "Welcome to the main page!"

def init_db():
    db = mysql.connector.connect(**DATABASE_CONFIG)
    cursor = db.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(255) NOT NULL,
        password VARCHAR(255) NOT NULL
    );
    ''')
    db.commit()
    db.close()

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']  # Remember: hash this password for security.
        
        db = mysql.connector.connect(**DATABASE_CONFIG)
        cursor = db.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        db.commit()
        db.close()
        
        return redirect(url_for('index'))
    
    return render_template('signup.html')

if __name__ == "__main__":
    init_db()  # Initialize the database on startup
    app.run(debug=True)
```

4. **`signup.html`**:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Signup Page</title>
</head>
<body>
    <h1>Signup</h1>
    <form method="post" action="/signup">
        <label for="username">Username:</label>
        <input type="text" name="username" required><br><br>

        <label for="password">Password:</label>
        <input type="password" name="password" required><br><br>

        <input type="submit" value="Signup">
    </form>
    <br>
    <a href="/">Back to Names</a>
</body>
</html>
```

Make sure to replace `'your_host'`, `'your_username'`, `'your_password'`, and `'your_database'` with the appropriate values for your MySQL setup.

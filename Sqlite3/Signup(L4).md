## Signup_Page

**Directory structure**:

```
/your_project_folder
    /templates
        index.html
        signup.html
    app.py
```

**1. `signup.html` inside the `templates` folder**:

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

**2. Update `app.py`**:

First, adjust the database initialization to account for a `users` table.

```python
def init_db():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS names (
        firstname TEXT NOT NULL
    );
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        username TEXT NOT NULL,
        password TEXT NOT NULL
    );
    ''')
    db.commit()
    db.close()
```

Then, add routes for rendering the signup page and processing signups.

```python
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']  # In a real-world scenario, you should hash this password.
        db = sqlite3.connect(DATABASE)
        cursor = db.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        db.commit()
        db.close()
        return redirect(url_for('index'))  # Redirect to the main page after successful signup.
    return render_template('signup.html')
```

**Note**: This is a basic example and not suitable for a production application. For security:

1. Passwords should never be stored in plain text; they should be hashed and salted (e.g., using libraries like `bcrypt`).
2. Input should be validated and sanitized to prevent SQL injection attacks or other vulnerabilities.
3. Consider using `Flask-Login` or `Flask-Security` extensions for handling user authentication and sessions in a more robust way.
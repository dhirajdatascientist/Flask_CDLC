**Directory structure**:

```
/your_project_folder
    /templates
        login.html
    app.py
```

**1. `login.html` in the `templates` folder**:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Login Page</title>
</head>
<body>
    <h1>Login</h1>
    <form method="post" action="/login">
        <input type="text" name="username" placeholder="Username"><br><br>
        <input type="password" name="password" placeholder="Password"><br><br>
        <input type="submit" value="Login">
    </form>
</body>
</html>
```

**2. `app.py`**:

```python
from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

DATABASE = 'emp.db'

def init_db():
    with sqlite3.connect(DATABASE) as db:
        db.execute('''
            CREATE TABLE IF NOT EXISTS users (
                username TEXT NOT NULL,
                password TEXT NOT NULL
            );
        ''')

init_db()

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        with sqlite3.connect(DATABASE) as db:
            cursor = db.cursor()
            cursor.execute("SELECT password FROM users WHERE username=?", (username,))
            stored_password = cursor.fetchone()

        if stored_password and stored_password[0] == password:
            return "Logged in successfully!"
        else:
            return "Invalid credentials. Try again."

    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
```

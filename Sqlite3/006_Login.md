## Without SQL 

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

**2. Minimal update for `app.py`**:

```python
from flask import Flask, request, render_template, redirect

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == "admin" and password == "password":  # Just for example, hardcoded credentials.
            return "Logged in successfully!"
        else:
            return "Invalid credentials. Try again."

    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
```
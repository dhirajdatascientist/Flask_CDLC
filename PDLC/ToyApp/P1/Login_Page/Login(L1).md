### 🌟 **Adding a Login Page to Flask** 🌟

#### 1️⃣ **Directory Structure**:

Update your directory to include the new template:

```
your_project_directory/
│
├── static/
│   ├── product1.jpg
│   ├── product2.jpg
│   └── product3.jpg
├── templates/
│   ├── base.html
│   ├── product.html
│   ├── services.html
│   ├── contact.html
│   └── login.html  <-- New File
└── app.py
```

#### 2️⃣ **Creating the Login Template**:

Inside the `templates` folder, create a new file called `login.html`:

```html
{% extends "base.html" %}

{% block content %}
<h2>Login</h2>
<form method="post">
    <div class="form-group">
        <label for="username">Username:</label>
        <input type="text" class="form-control" id="username" name="username" required>
    </div>
    <div class="form-group">
        <label for="password">Password:</label>
        <input type="password" class="form-control" id="password" name="password" required>
    </div>
    <button type="submit" class="btn btn-primary">Login</button>
</form>
{% endblock %}
```

#### 3️⃣ **Updating `app.py`**:

Extend your `app.py` to handle the login:

```python
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'some_secret_key'  # Needed for flashing messages

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/product')
def product():
    return render_template('product.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'admin':
            flash('Login successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid credentials. Please try again.', 'danger')
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
```

Note: We've added a secret key for Flask's session to work, which is required for the flash messages.

#### 4️⃣ **Update the Navbar**:

Modify `base.html` to include a "Login" link:

```html
<!-- ... (rest of the navbar code) ... -->
<ul class="navbar-nav mr-auto">
    <!-- ... (other nav items) ... -->
    <li class="nav-item">
        <a class="nav-link" href="/login">Login</a>
    </li>
</ul>
<!-- ... (rest of the navbar code) ... -->
```

#### 5️⃣ **Running the Application**:

1. Ensure your virtual environment (`venv`) is active.
2. Run the Flask app:
    ```bash
    python app.py
    ```

3. **Access Your Flask App**:

Open a web browser and navigate to:

```
http://127.0.0.1:5000/login
```

You can now try logging in with the username `admin` and password `admin`. Upon a successful login, a flash message will display, and you'll be redirected to the homepage. If you enter wrong credentials, an error message will show up.

Remember: This is a simple hardcoded authentication example, and is not suitable for a production environment. For a production environment, consider using tools like Flask-Login and storing hashed passwords in a database.
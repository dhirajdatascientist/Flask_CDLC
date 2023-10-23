## Flask

1. Flask Setup with Random Secret Key:

```python
from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
```

2. Database Models:

```python
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)  # Still plain-text; you should use hashed passwords
    data = db.relationship('Data', backref='owner', lazy=True)

class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(1000), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
```

3. User Login and Data Management:

```python
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid credentials', 'danger')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    if request.method == 'POST':
        new_data = Data(content=request.form.get('content'), user_id=current_user.id)
        db.session.add(new_data)
        db.session.commit()
        flash('Data added successfully!', 'success')
    user_data = Data.query.filter_by(user_id=current_user.id).all()
    return render_template('dashboard.html', data=user_data)
```

4. Run the Flask App:

```python
if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
```

Now, for the templates, let's assume you'll place them in a folder named `templates`.

a) `templates/login.html`:
```html
<!DOCTYPE html>
<html>
<head>
    <title>Login</title>
</head>
<body>
    <form action="{{ url_for('login') }}" method="post">
        <label>Username:</label>
        <input type="text" name="username">
        <br>
        <label>Password:</label>
        <input type="password" name="password">
        <br>
        <button type="submit">Login</button>
    </form>
</body>
</html>
```

b) `templates/dashboard.html`:
```html
<!DOCTYPE html>
<html>
<head>
    <title>Dashboard</title>
</head>
<body>
    <h2>Welcome, {{ current_user.username }}</h2>
    <form action="{{ url_for('dashboard') }}" method="post">
        <textarea name="content"></textarea>
        <br>
        <button type="submit">Add Data</button>
    </form>

    <h3>Your Data:</h3>
    <ul>
        {% for item in data %}
            <li>{{ item.content }}</li>
        {% endfor %}
    </ul>

    <a href="{{ url_for('logout') }}">Logout</a>
</body>
</html>
```

Please note:
- This is a basic implementation.
- Passwords are stored in plain text, which is not secure. Use something like `Flask-Bcrypt` for hashing and checking passwords.
- Implement registration or manually add users to the database to login.
- Add error handling and additional features as needed.
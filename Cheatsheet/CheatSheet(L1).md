# CheatSheet

### 1. Hello World App:

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()
```

### 2. Route Parameters:

```python
@app.route('/user/<username>')
def user_profile(username):
    return f'User: {username}'
```

### 3. HTTP Methods:

```python
@app.route('/submit', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        # Handle POST request here
```

### 4. Redirects:

```python
from flask import redirect, url_for

@app.route('/redirect')
def redirect_example():
    return redirect(url_for('other_route'))
```

### 5. Templates:

```python
from flask import render_template

@app.route('/template')
def render_template_example():
    return render_template('template.html', var_name=data)
```

### 6. Template Inheritance (base.html and child.html):

**base.html:**

```html
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}{% endblock %}</title>
</head>
<body>
    {% block content %}{% endblock %}
</body>
</html>
```

**child.html:**

```html
{% extends "base.html" %}
{% block title %}Child Title{% endblock %}
{% block content %}
<!-- Child content here -->
{% endblock %}
```

### 7. Handling Forms:

```python
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Handle form submission
    else:
        # Render the form
```

### 8. Flask-WTF for Forms:

```python
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class MyForm(FlaskForm):
    name = StringField('Name')
    submit = SubmitField('Submit')
```

### 9. SQLAlchemy for Database Integration:

```python
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
```

### 10. Flask-Login for User Sessions:

```python
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
```

### 11. Flask-RESTful for RESTful APIs:

```python
from flask_restful import Resource, Api

api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'message': 'Hello, World!'}

api.add_resource(HelloWorld, '/')
```


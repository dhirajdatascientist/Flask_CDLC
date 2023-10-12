### Simple Flask-WTForms Application Setup:

**1. Install dependencies**:
```bash
pip install Flask Flask-WTF
```

**2. `app.py`:** 
```python
from flask import Flask, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey' 

class MyForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = MyForm()
    if form.validate_on_submit():
        flash(f'Hello, {form.name.data}!', 'success')
        return redirect(url_for('index'))
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
```

**3. Set up templates**:
```bash
mkdir templates
```

**4. `templates/index.html`:** 
```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>WTF in Flask</title>
  </head>
  <body>
    <div>
      {% with messages = get_flashed_messages(with_categories=true) %}
        {% if messages %}
          {% for category, message in messages %}
            <div class="{{ category }}">{{ message }}</div>
          {% endfor %}
        {% endif %}
      {% endwith %}
      <form method="post" action="{{ url_for('index') }}">
        {{ form.hidden_tag() }}
        <div>{{ form.name.label }}<br>{{ form.name() }}</div>
        <div>{{ form.submit() }}</div>
      </form>
    </div>
  </body>
</html>
```

**5. Run the app**:
```bash
python app.py
```


This is a compact guide to setting up a Flask app with WTForms using the Flask-WTF extension.


**Explanation**

**1. Install dependencies**:

- `Flask-WTF`: An extension for Flask that integrates the use of WTForms, which is a form handling library in Python.


**2. `app.py`**:

This Python script sets up the Flask application.

- **Imports**:
  - `Flask, render_template, redirect, url_for, flash`: Core Flask functions for setting up the web app, rendering templates, redirecting, generating URLs, and flashing messages.
  - `FlaskForm`: Base class for creating WTForms in a Flask application.
  - `StringField, SubmitField`: Form fields.
  - `DataRequired`: A validator to ensure that the field is not submitted empty.

- `app = Flask(__name__)`: Initializes the Flask application instance.
  
- `app.config['SECRET_KEY'] = 'mysecretkey'`: Sets a secret key for the Flask application. This is necessary for session security, especially for protecting against cross-site request forgery attacks.

- `class MyForm(FlaskForm)`: Defines a simple form with a name field and a submit button.

- `@app.route(...)`: Defines a route for the root URL ("/") which can handle both GET and POST requests. If the form is submitted and is valid, it flashes a greeting message and redirects to the index. If not, it renders the template `index.html` with the form.

---

**3. Set up templates**:
This command creates a directory named `templates`. Flask by default looks for HTML templates in a folder named `templates`.
```bash
mkdir templates
```

---

**4. `templates/index.html`**:

This is the HTML template for the root route. It uses the Jinja2 templating language, which is integrated with Flask.

- `{% with messages = get_flashed_messages(with_categories=true) %}`: Grabs any flashed messages from Flask's `flash` function. Messages can also have categories, which are essentially tags.

- The `form` block creates an HTML form, where:
  - `{{ form.hidden_tag() }}`: Renders a hidden CSRF token field for security.
  - `{{ form.name.label }}` and `{{ form.name() }}`: Renders the label and input for the `name` field of the form.
  - `{{ form.submit() }}`: Renders the submit button of the form.

---

**5. Run the app**:
Finally, to start the Flask development server and run the app, use:
```bash
python app.py
```
This will start the app, and by default, it will be accessible at `http://127.0.0.1:5000/`. Any changes made to the app (because `debug=True`) will be reflected upon reloading the page, but be cautious about using debug mode in a production environment.

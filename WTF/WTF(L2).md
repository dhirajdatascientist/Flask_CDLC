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

---

This is a compact guide to setting up a Flask app with WTForms using the Flask-WTF extension.
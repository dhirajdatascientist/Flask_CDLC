## Flashed Message

1. **`app.py`**:

```python
import secrets
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)  # Generates a random key with 32 characters

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    flash('You clicked the button!')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
```

2. **`templates/index.html`**:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Flash Messages in Flask with Random Secret Key</title>
</head>
<body>

<div>
    {% with messages = get_flashed_messages() %}
        {% if messages %}
            <ul>
            {% for message in messages %}
                <li>{{ message }}</li>
            {% endfor %}
            </ul>
        {% endif %}
    {% endwith %}
</div>

<form method="post" action="/process">
    <button type="submit">Click Me</button>
</form>

</body>
</html>
```

To run the application:

1. Save the first code block in a file named `app.py`.
2. Create a folder named `templates` in the same directory.
3. Inside the `templates` folder, save the second code block in a file named `index.html`.
4. Run the Flask application with the command `python app.py`.


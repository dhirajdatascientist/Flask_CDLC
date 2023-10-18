1. Set up your directory structure:

```
/your_project_folder
    /templates
        index.html
    app.py
```

2. Create the `index.html` inside the `templates` folder:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Names App</title>
</head>
<body>
    <h1>Names</h1>
    <ul>
    {% for name in names %}
        <li>{{ name[0] }}</li>
    {% endfor %}
    </ul>
    <form method="post" action="/add">
        <input type="text" name="firstname" placeholder="First Name" required>
        <input type="submit" value="Add Name">
    </form>
</body>
</html>
```

3. Update `app.py`:

```python
from flask import Flask, request, render_template, redirect, url_for
import sqlite3

app = Flask(__name__)

DATABASE = 'names.db'

def init_db():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS names (
        firstname TEXT NOT NULL
    );
    ''')
    db.commit()
    db.close()

init_db()

@app.route('/')
def index():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    cursor.execute("SELECT firstname FROM names")
    names = cursor.fetchall()
    db.close()
    return render_template('index.html', names=names)

@app.route('/add', methods=['POST'])
def add_name():
    firstname = request.form['firstname']
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    cursor.execute("INSERT INTO names (firstname) VALUES (?)", (firstname,))
    db.commit()
    db.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
```

Now, when you run `app.py`, Flask will automatically use the `index.html` template from the `templates` folder. 
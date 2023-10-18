## Storing first name in Database.

```python
from flask import Flask, request, render_template_string, redirect, url_for
import sqlite3

app = Flask(__name__)

DATABASE = 'names.db'

# Initialize the database and create table if it doesn't exist
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
    return render_template_string('''
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
    ''', names=names)

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

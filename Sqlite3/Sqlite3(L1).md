### Step 1: Set Up the Flask Application
Firstly, install Flask using pip if you haven't already:
```bash
pip install Flask
```

Then, create your main Flask application file, e.g., `app.py`:
```python
from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/submit_form", methods=["POST"])
def submit_form():
    name = request.form.get("name")
    with sqlite3.connect("data.db") as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (name) VALUES (?)", (name,))
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
```
### Step 2: Set Up SQLite Database
Create a SQLite database named `data.db` with a table for user data:

In Python, you might create and initialize your SQLite database like this:

```python
import sqlite3

conn = sqlite3.connect('data.db')
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name TEXT
)
''')
conn.commit()
conn.close()
```

### Step 3: Create HTML Templates
Now create a directory named `templates`, and in that directory, create an HTML file named `index.html`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simple Form</title>
</head>
<body>
    <h1>Simple Form</h1>
    <form method="POST" action="/submit_form">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        <input type="submit" value="Submit">
    </form>
</body>
</html>
```
### Step 4: Run the Flask Application
Finally, run your Flask application by executing `app.py`:

```bash
python app.py
```
Your application should now be running on `http://127.0.0.1:5000/` or `http://localhost:5000/`.

### Explanation
- **Flask Setup**: The basic Flask setup involves importing necessary modules, defining routes, and running the app.
- **SQLite Setup**: SQLite is used to store the form data. Ensure you've created the database and table before running the Flask app.
- **HTML Form**: The form is rendered using Flask's `render_template` and it `POST`s data to the `/submit_form` endpoint.
- **Form Submission**: When the form is submitted, the name data is added to the SQLite database, and the user is redirected back to the home page.

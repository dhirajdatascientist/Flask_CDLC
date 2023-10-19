1. **Setup**

First, install the necessary libraries:

```bash
pip install Flask Flask-SQLAlchemy
```

2. **Flask App**

Let's structure our app. 

Directory structure:
```
/audio_app
    /templates
        index.html
    app.py
    database.db
```

3. **app.py**

```python
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'wav', 'mp3'}

db = SQLAlchemy(app)

class Audio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(300))
    data = db.Column(db.LargeBinary)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            new_file = Audio(filename=file.filename, data=file.read())
            db.session.add(new_file)
            db.session.commit()
            return redirect(url_for('index'))
    
    return render_template('index.html')

if __name__ == '__main__':
    if not os.path.exists('database.db'):
        db.create_all()
    app.run(debug=True)
```

4. **index.html** in `/templates`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Audio Upload</title>
</head>
<body>
    <form action="/" method="POST" enctype="multipart/form-data">
        <input type="file" name="file">
        <input type="submit" value="Upload">
    </form>
</body>
</html>
```

5. **Running the App**

In the terminal, navigate to the `/audio_app` directory and run:

```bash
python app.py
```

This will start a local server. Navigate to `http://127.0.0.1:5000/` in your browser, and you should be able to upload an audio file. The file's binary data will be stored in the SQLite3 database.
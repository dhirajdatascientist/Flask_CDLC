## To integrate SQLite3 with Flask

```python
from flask import Flask
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    conn = sqlite3.connect('mydatabase.db')
    if conn:
        message = "Connected to the database successfully!"
    conn.close()
    
    return message

if __name__ == "__main__":
    app.run()
```

To run the Flask app:

1. Install Flask:
```
pip install Flask
```

2. Save the above code to a file, e.g., `app.py`.

3. Run the app:
```
python app.py
```

4. Visit `http://127.0.0.1:5000/` in your browser. You should see a success message if the connection was successful or an error message otherwise.

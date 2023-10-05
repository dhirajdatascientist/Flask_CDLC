
```python
from flask import Flask

# Create a Flask web application
app = Flask(__name__)

# Define a route for the root URL ("/")
@app.route('/')
def hello_world():
    return 'Hello, World!'

# Run the application if this script is executed
app.run()
```

3. Save the `app.py` file.

4. Open your terminal and navigate to the directory where `app.py` is located.

5. Run the Flask application:

```bash
python app.py
```

You'll see output indicating that the Flask development server is running, and it should tell you the address where the server is running (usually http://127.0.0.1:5000/).

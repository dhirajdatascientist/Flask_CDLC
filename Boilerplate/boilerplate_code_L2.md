1. Install Flask (if you haven't already) using pip:

```
pip install Flask
```

2. Create a folder for your Flask application. Inside this folder, create the following directory structure:

```
your_app_folder/
    templates/
        hello.html
    app.py
```

3. In the `hello.html` file inside the `templates` folder, add the following HTML content:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Hello World</title>
</head>
<body>
    <h1>Hello, World!</h1>
</body>
</html>
```

4. In the `app.py` file, create your Flask application and render the `hello.html` template:

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('hello.html')

if __name__ == '__main__':
    app.run(debug=True)
```

5. Save the `app.py` file.

6. To run your Flask application, open a terminal, navigate to your app's folder, and run the following command:

```
python app.py
```

This will start the Flask development server, and you should see output similar to:

```
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

7. Open a web browser and navigate to `http://127.0.0.1:5000/` or `http://localhost:5000/`. You should see the "Hello, World!" message displayed in your browser.

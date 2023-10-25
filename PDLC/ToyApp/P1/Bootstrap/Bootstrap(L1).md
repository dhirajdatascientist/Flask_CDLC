### 🌟 **Complete Guide: Flask with Bootstrap** 🌟

#### 1️⃣ **Virtual Environment & Flask Installation** (As previously mentioned):

1. **Open Command Prompt**.
2. **Navigate to Your Project Directory**:
    ```bash
    cd path_to_your_project_directory
    ```
3. **Create the Virtual Environment**:
    ```bash
    python -m venv venv
    ```
4. **Activate the Virtual Environment**:
    ```bash
    .\venv\Scripts\activate
    ```
5. **Install Flask**:
    ```bash
    pip install Flask
    ```

#### 2️⃣ **Directory Structure**:

Ensure your directory structure is organized as follows:
```
your_project_directory/
│
├── venv/
├── templates/
│   ├── base.html
│   └── home.html
└── app.py
```

#### 3️⃣ **Setting Up Bootstrap with Flask Templates**:

1. **Modify `base.html` with Bootstrap**:

Inside the `templates` folder, open or create `base.html`. Add the following content:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
    <title>{% block title %}Default Title{% endblock %}</title>
</head>
<body>
    <header class="navbar navbar-dark bg-dark">
        <div class="container-fluid">
            <a class="navbar-brand" href="#">My Flask App</a>
        </div>
    </header>
    
    <main class="container mt-4">
        {% block content %}
        <!-- Main content will go here -->
        {% endblock %}
    </main>

    <footer class="footer mt-auto py-3 bg-light">
        <div class="container">
            <span class="text-muted">Footer content here.</span>
        </div>
    </footer>
    <!-- Optional Bootstrap JS -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-alpha1/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
```

2. **Modify `home.html`**:

Inside the `templates` folder, open or create `home.html`:

```html
{% extends "base.html" %}

{% block title %}
Home Page
{% endblock %}

{% block content %}
<div class="jumbotron">
    <h1 class="display-4">Welcome to our website!</h1>
    <p class="lead">This is the homepage content using Bootstrap.</p>
    <hr class="my-4">
    <p>More description can go here.</p>
    <a class="btn btn-primary btn-lg" href="#" role="button">Learn more</a>
</div>
{% endblock %}
```

3. **Setting Up Flask in `app.py`**:

In your project's root directory, open or create `app.py`:

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
```

#### 4️⃣ **Running the Application**:

1. Ensure your virtual environment (`venv`) is still active.
2. Run the Flask app:
    ```bash
    python app.py
    ```

3. **Access Your Flask App**:

Open a web browser and navigate to:

```
http://127.0.0.1:5000/
```

You should now see a Bootstrap-enhanced web page, which is your Flask app's homepage.

#### 5️⃣ **Exit**:

When done working on your Flask project, deactivate your virtual environment:
```bash
deactivate
```


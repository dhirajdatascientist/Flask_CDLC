## Adding Navbar

### 🌟 **Simplified Guide: Flask with Bootstrap's "ToyApp" Navbar** 🌟

#### 1️⃣ **Directory Structure**:

Your directory should look like:
```
your_project_directory/
│
├── templates/
│   └── base.html
└── app.py
```

#### 2️⃣ **Setting Up Bootstrap with Flask Templates**:

1. **Modify `base.html` with Bootstrap and ToyApp Navbar**:

Inside the `templates` folder, create or modify `base.html` to contain:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
    <title>{% block title %}ToyApp{% endblock %}</title>
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <div class="container-fluid">
            <a class="navbar-brand" href="#">ToyApp</a>
        </div>
    </nav>
    
    <main class="container mt-4">
        {% block content %}
        <!-- Main content will go here -->
        {% endblock %}
    </main>

    <!-- Optional Bootstrap JS -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-alpha1/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
```

2. **Setting Up Flask in `app.py`**:

In your project's root directory, create or modify `app.py`:

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('base.html')

if __name__ == '__main__':
    app.run(debug=True)
```

#### 3️⃣ **Running the Application**:

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

You should now see a Bootstrap-enhanced web page with a navbar titled "ToyApp".
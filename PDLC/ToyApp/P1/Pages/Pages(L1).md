### 🌟 **Adding Product, Services, and Contact Pages to Flask with Bootstrap** 🌟

#### 1️⃣ **Directory Structure**:

Your directory should look something like this after adding the three pages:

```
your_project_directory/
│
├── templates/
│   ├── base.html
│   ├── product.html
│   ├── services.html
│   └── contact.html
└── app.py
```

#### 2️⃣ **Modifying Navbar in `base.html`**:

Update the navbar in `base.html` to include links for the three new pages:

```html
<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <div class="container-fluid">
        <a class="navbar-brand" href="/">ToyApp</a>
        <div class="collapse navbar-collapse">
            <ul class="navbar-nav mr-auto">
                <li class="nav-item">
                    <a class="nav-link" href="/product">Product</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="/services">Services</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="/contact">Contact</a>
                </li>
            </ul>
        </div>
    </div>
</nav>
```

#### 3️⃣ **Creating the New Templates**:

Inside the `templates` folder:

1. **product.html**:

```html
{% extends "base.html" %}

{% block content %}
<h2>Product</h2>
<p>Welcome to our product page! Here, you can find the best toys in the market.</p>
{% endblock %}
```

2. **services.html**:

```html
{% extends "base.html" %}

{% block content %}
<h2>Services</h2>
<p>We offer a range of services, including toy repair and customization.</p>
{% endblock %}
```

3. **contact.html**:

```html
{% extends "base.html" %}

{% block content %}
<h2>Contact</h2>
<p>Have questions? Reach out to us at toyapp@email.com.</p>
{% endblock %}
```

#### 4️⃣ **Updating `app.py`**:

Extend your `app.py` to serve the new pages:

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/product')
def product():
    return render_template('product.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
```

#### 5️⃣ **Running the Application**:

1. Ensure your virtual environment (`venv`) is active.
2. Run the Flask app:
    ```bash
    python app.py
    ```

3. **Access Your Flask App**:

Open a web browser and navigate to:

```
http://127.0.0.1:5000/
```

From here, you can navigate using the links on the navbar to visit the Product, Services, and Contact pages.

You've now extended your Flask application to include three new pages, each having its own content and accessible via the navbar in the `base.html` template.
# First Templates
* Using templates is a fundamental aspect of Flask. 
* It allows for dynamic content generation on web pages. 
* For this, Flask uses the Jinja2 templating engine. 
* One of the benefits of Jinja2 is that it allows you to create base templates and extend them, which is great for maintaining a consistent look and feel across your web pages.

Let's create a base template and extend it.

### 📁 Setting Up Templates

1. **Directory Structure**:
    In your project directory, create a new folder named `templates`. This is where Flask expects to find the Jinja2 templates.
    ```
    your_project_directory/
    │
    ├── venv/
    ├── templates/
    │   └── base.html  # We'll create this soon
    ├── app.py
    ```

2. **Creating `base.html`**:
    Within the `templates` folder, create a file named `base.html`. This will be our base template.

    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{% block title %}Default Title{% endblock %}</title>
    </head>
    <body>
        <header>
            <!-- You can put a standard header content here -->
        </header>
        
        <main>
            {% block content %}
            <!-- Main content will go here -->
            {% endblock %}
        </main>

        <footer>
            <!-- Standard footer content -->
        </footer>
    </body>
    </html>
    ```

    Here, `{% block title %}` and `{% block content %}` are block tags. They define regions of the template that child templates (templates that extend this base) can fill in.

3. **Extending `base.html`**:
    Let's say you want to create a homepage. You can make a `home.html` template that extends the `base.html`:

    `home.html` (within the `templates` folder):

    ```html
    {% extends "base.html" %}

    {% block title %}
    Home Page
    {% endblock %}

    {% block content %}
    <h1>Welcome to our website!</h1>
    <p>This is the homepage content.</p>
    {% endblock %}
    ```

4. **Render the Template in `app.py`**:
    Adjust your `app.py` to render the `home.html`:

    ```python
    from flask import Flask, render_template
    app = Flask(__name__)

    @app.route('/')
    def home():
        return render_template('home.html')

    if __name__ == '__main__':
        app.run(debug=True)
    ```

5. **Run and Test**:
    If you run `python app.py` and visit `http://127.0.0.1:5000/`, you should see the content from both `base.html` and `home.html` combined. The homepage content should be inserted where the `content` block is in `base.html`, and the title should change to "Home Page".

---

This method of templating keeps your HTML organized and allows you to maintain a consistent look across multiple pages. As your application grows, you can continue to extend the `base.html` for other pages.
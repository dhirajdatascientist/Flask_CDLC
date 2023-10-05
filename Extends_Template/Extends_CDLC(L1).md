# To extend an HTML file in Flask, 

* You can use a template engine like Jinja2. 
* Jinja2 allows you to create reusable templates and extend them to build your web pages. Here's how you can extend an HTML file in Flask:

1. Create a Flask project directory with the following structure:

```
my_flask_app/
    templates/
        base.html
        child.html
    app.py
```

2. Install Flask if you haven't already:

```bash
pip install Flask
```

3. Create your base HTML template (`base.html`) inside the `templates` folder. This template will define the overall structure of your web pages and include placeholders for content that will be extended in child templates.

`base.html`:
```html
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}My Flask App{% endblock %}</title>
</head>
<body>
    <header>
        <h1>{% block header %}Welcome to My Flask App{% endblock %}</h1>
    </header>
    
    <nav>
        <ul>
            <li><a href="/">Home</a></li>
            <li><a href="/about">About</a></li>
        </ul>
    </nav>
    
    <main>
        {% block content %}{% endblock %}
    </main>
</body>
</html>
```

In this template, you define several blocks (`title`, `header`, and `content`) that can be overridden in child templates.

4. Create a child HTML template (`child.html`) that extends the `base.html` template and fills in the content block.

`child.html`:
```html
{% extends "base.html" %}

{% block title %}About Us - My Flask App{% endblock %}

{% block header %}About Us{% endblock %}

{% block content %}
    <h2>About Our Company</h2>
    <p>We are a fantastic company doing amazing things.</p>
{% endblock %}
```

In this template, you use `{% extends "base.html" %}` to indicate that it extends the `base.html` template and then override the `title`, `header`, and `content` blocks with content specific to the "About Us" page.

5. Create your Flask application (`app.py`) and render the child template in a route:

`app.py`:
```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('child.html')

if __name__ == '__main__':
    app.run(debug=True)
```

6. Run your Flask application:

```bash
python app.py
```

Now, when you visit the home page (`http://127.0.0.1:5000/`), it will render the `child.html` template, which extends the `base.html` template and fills in the content block specific to the "About Us" page.

You can create more child templates and extend the `base.html` template for different pages of your website while maintaining a consistent layout and structure.
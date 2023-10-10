
# FoodApp
* Creating a food booking app using Flask and MongoDB involves several steps, including setting up the project, creating the database schema, developing the Flask application, and designing the HTML templates. 

**Step 1: Project Setup**

1. Create a new directory for your project and navigate to it in your terminal.

2. Set up a virtual environment to isolate your project's dependencies:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate
   ```

3. Install the required packages using pip:

   ```bash
   pip install Flask Flask-PyMongo
   ```

4. Create a new MongoDB database for your app. Make note of the connection URL.

**Step 2: Create MongoDB Schema**

In this example, we'll create a simple schema with two collections: 'restaurants' and 'bookings'.

**Step 3: Create the Flask Application**

Create a Python script for your Flask application, e.g., `app.py`.

```python
from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost/your-database-name'  # Update with your MongoDB URI
mongo = PyMongo(app)

# Define routes and views

if __name__ == '__main__':
    app.run(debug=True)
```

**Step 4: Create HTML Templates**

Create a `templates` folder in your project directory and add the following HTML templates:

1. `layout.html` - A common layout for your app.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Food Booking App</title>
</head>
<body>
    <h1>Food Booking App</h1>
    <hr>
    {% block content %}{% endblock %}
</body>
</html>
```

2. `index.html` - The homepage to display restaurants.

```html
{% extends 'layout.html' %}

{% block content %}
    <h2>Restaurants</h2>
    <ul>
        {% for restaurant in restaurants %}
            <li>
                <strong>{{ restaurant.name }}</strong> - {{ restaurant.cuisine }}
                <a href="{{ url_for('book', restaurant_id=restaurant._id) }}">Book</a>
            </li>
        {% endfor %}
    </ul>
{% endblock %}
```

3. `booking.html` - Page for making bookings.

```html
{% extends 'layout.html' %}

{% block content %}
    <h2>Book a Table</h2>
    <form method="POST" action="{{ url_for('book', restaurant_id=restaurant_id) }}">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        <br>
        <label for="date">Date:</label>
        <input type="date" id="date" name="date" required>
        <br>
        <button type="submit">Book Now</button>
    </form>
{% endblock %}
```

**Step 5: Define Flask Routes and Database Interactions**

In your `app.py` file, define the routes for displaying restaurants, making bookings, and handling form submissions.

```python
from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost/your-database-name'  # Update with your MongoDB URI
mongo = PyMongo(app)

# Define routes and views
@app.route('/')
def index():
    restaurants = mongo.db.restaurants.find()
    return render_template('index.html', restaurants=restaurants)

@app.route('/book/<restaurant_id>', methods=['GET', 'POST'])
def book(restaurant_id):
    if request.method == 'POST':
        name = request.form.get('name')
        date = request.form.get('date')
        booking = {
            'restaurant_id': restaurant_id,
            'name': name,
            'date': date
        }
        mongo.db.bookings.insert_one(booking)
        return redirect(url_for('index'))
    else:
        return render_template('booking.html', restaurant_id=restaurant_id)

if __name__ == '__main__':
    app.run(debug=True)
```

**Step 6: Run the Application**

In your terminal, run the Flask application:

```bash
python app.py
```

Food booking app should now be accessible at `http://localhost:5000`.

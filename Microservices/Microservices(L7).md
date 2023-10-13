## Answer for Microservices(L5)

### 1. Basic Flask Application
```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_india():
    return "Hello, India!"
```
* The base structure of a Flask application remains simple and clear.
* A new route is defined for the root URL ("/") and associated with the `hello_india()` function.
* When visited, it sends back the message "Hello, India!" instead of "Hello, World!".

### 2. Personalized Morning Greet
```python
@app.route('/morning/<name>')
def morning(name):
    return f"Good Morning, {name}!"
```
* The URL variable `<name>` allows a dynamic path segment.
* Navigating to `/morning/[some_name]`, triggers `morning()`, greeting the user with "Good Morning, [some_name]!".

### 3. Age-Based Category Determination
```python
@app.route('/age-category')
def age_category():
    age = int(request.args.get('age', 0))
    return "Senior Citizen" if age >= 60 else "Not a Senior Citizen"
```
* Query parameters (e.g., `/age-category?age=65`) are leveraged to obtain age.
* A basic condition now checks if the user is a Senior Citizen or not.

### 4. Echo JSON Data
```python
@app.route('/echo-json', methods=['POST'])
def echo_json():
    return jsonify(request.json)
```
* POST requests are handled and echoed back as a JSON response.
* `jsonify` ensures that Python data structures are converted and returned as JSON.

### 5. Admin Access Validation
```python
@app.route('/admin')
def admin():
    auth = request.authorization
    if not auth or not check_auth(auth.username, auth.password):
        return Response('Access Denied', 403)
    return "Admin page!"
```
* HTTP authentication is employed.
* Invalid or absent credentials lead to an "Access Denied" message and a 403 status code.

* Complete Code
```
from flask import Flask, request, Response

app = Flask(__name__)

def check_auth(username, password):
    return username == 'admin' and password == 'secret'

@app.route('/admin')
def admin():
    auth = request.authorization
    
    if not auth or not check_auth(auth.username, auth.password):
        return Response('Access Denied', 403, {'WWW-Authenticate': 'Basic realm="Login required!"'})
    
    return "Admin page!"

if __name__ == "__main__":
    app.run(debug=True)
```


### 6. Retrieve User Agent Info
```python
@app.route('/browser-info')
def browser_info():
    return request.headers.get('User-Agent')
```
* The user-agent string is fetched and returned.
* This string provides details like browser type and version, and OS information.

### 7. Multiply Two Query Parameters
```python
@app.route('/multiply')
def multiply():
    a = int(request.args.get('a', 1))
    b = int(request.args.get('b', 1))
    return str(a * b)
```
* Parameters `a` and `b` are fetched, multiplied, and the result is returned as a string.

### 8. Blueprint for Categories
```python
categories = Blueprint('categories', __name__)

@categories.route('/')
def category_list():
    return "List of categories"

app.register_blueprint(categories, url_prefix='/categories')
```
* A blueprint named `categories` is defined and registered.
* Associated with its own route, it’s set up under the `/categories` prefix.

### 9. Basic REST API for Note Entity (pseudo-code)
```python
notes = []

@app.route('/notes', methods=['GET', 'POST'])
def manage_notes():
    if request.method == 'GET':
        return jsonify(notes)
    else:
        notes.append(request.json)
        return "Note added!", 201
```
* The REST API manages a 'notes' list.
* GET requests retrieve all notes, while POST requests add a new note, responding with a 201 status code.

### 10. Logging Middleware
```python
@app.before_request
def log_user_agent():
    print(f"{request.method} {request.path} - User Agent: {request.headers.get('User-Agent')}")
```
* Using Flask's `before_request` hook, logging middleware is implemented.
* This logs the request method, path, and user-agent string before processing each request.

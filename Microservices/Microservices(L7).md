## Answer for Microservices(L5)

### 1. Basic Flask Application
```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, World!"
```
* This is the fundamental structure of a Flask application. 
* The Flask instance `app` is created and a route is defined for the root URL ("/"). 
* When a user visits this URL, the `hello_world()` function is triggered and sends back the message "Hello, World!".

### 2. Greet User by Name
```python
@app.route('/greet/<name>')
def greet(name):
    return f"Hello, {name}!"
```
* This route demonstrates URL variables in Flask, with `<name>` being a variable part of the URL. 
* When a user visits `/greet/[some_name]`, the `greet()` function gets triggered with the `name` parameter set to `[some_name]`, and a personalized greeting is returned.

### 3. Determine Adult or Minor based on Age
```python
from flask import request

@app.route('/check-age')
def check_age():
    age = int(request.args.get('age', 0))
    return "Adult" if age >= 18 else "Minor"
```
* This endpoint uses query parameters to obtain user input. 
* The `age` parameter is retrieved from the URL (e.g., `/check-age?age=20`) and is used to determine if the user is an adult or a minor. 
* This is accomplished through a simple conditional expression.

### 4. Return JSON Data Received
```python
from flask import request, jsonify

@app.route('/post-json', methods=['POST'])
def post_json():
    return jsonify(request.json)
```
* This snippet handles POST requests and sends back the received JSON data as a response. 
* The `jsonify` function converts Python dictionaries or lists to JSON format. 
* This route is often used in API development to accept JSON payloads.

### 5. Basic Authentication for a Flask Route
```python
from flask import Response

def check_auth(username, password):
    return username == 'admin' and password == 'password'

@app.route('/secret')
def secret():
    auth = request.authorization
    if not auth or not check_auth(auth.username, auth.password):
        return Response('Unauthorized', 401)
    return "Secret page!"
```
* This route demonstrates basic HTTP authentication. 
* The `check_auth` function validates a username and password, while the `/secret` route checks whether incoming requests have valid credentials before allowing access to a "secret" page. 
* Unauthorized access attempts receive a 401 response.

### 6. Return User Agent
```python
@app.route('/user-agent')
def user_agent():
    return request.headers.get('User-Agent')
```
* This route returns the user-agent string from the client's request headers, which typically provides information about the client's browser and operating system. 
* It is useful for logging or rendering content differently based on the user's browser.

### 7. Sum of Two Query Parameters
```python
@app.route('/add')
def add():
    a = int(request.args.get('a', 0))
    b = int(request.args.get('b', 0))
    return str(a + b)
```
* This demonstrates how to retrieve multiple query parameters and perform a calculation. 
* The parameters `a` and `b` are retrieved from the URL, summed, and the result is returned as a string.

### 8. Blueprint for Products
```python
from flask import Blueprint

products = Blueprint('products', __name__)

@products.route('/')
def product_list():
    return "List of products"

app.register_blueprint(products, url_prefix='/products')
```
* BluePrints in Flask are used to modularize routes, making them more organized and reusable. 
* Here, a blueprint named `products` is defined with its own route, which is registered with the main Flask app instance under the `/products` prefix.

### 9. Simple REST API for Todo Entity (pseudo-code)
```python
todos = []

@app.route('/todos', methods=['GET', 'POST'])
def manage_todos():
    if request.method == 'GET':
        return jsonify(todos)
    else:
        todos.append(request.json)
        return "Todo added!", 201
```
* A simple REST API for managing a 'todo' list. It responds to GET requests by returning all 'todos' and responds to POST requests by adding a new 'todo' to the list. 
* The use of status code 201 indicates successful creation of a resource on the server.

### 10. Middleware for Logging
```python
@app.before_request
def log_request():
    print(f"{request.method} {request.path}")
```
* Middleware for logging demonstrates how to use Flask's `before_request` hook to execute code before each request. 
* Here, each incoming request's method (GET, POST, etc.) and path are logged to the console before processing the request itself.


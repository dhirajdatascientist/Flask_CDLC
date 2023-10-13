## Asnwers of L6

### 11. Set Cookie in Flask Route
```python
from flask import make_response

@app.route('/set-cookie/<user_id>')
def set_cookie(user_id):
    resp = make_response("Cookie Set")
    resp.set_cookie('user_id', user_id)
    return resp
```
* A user ID is passed as a URL parameter and set as a cookie named `user_id` in the user’s browser.
* `make_response` is used to create a response object, which allows us to set additional HTTP headers, like cookies.

### 12. Read Cookie from Request
```python
@app.route('/read-cookie')
def read_cookie():
    session_id = request.cookies.get('session_id')
    return f"Session ID: {session_id}"
```
* This route fetches and displays the value of the `session_id` cookie.
* If the cookie is not present, `None` is returned and displayed.

### 13. Handle Errors with Custom JSON Response
```python
@app.errorhandler(404)
def not_found(error):
    return jsonify(error="Not Found", message="The resource was not found"), 404
```
* `@app.errorhandler` is a decorator that defines a custom error handler for the specified error code.
* Here, it catches 404 errors and returns a custom JSON message.

### 14. File Upload and Save
```python
from flask import request, redirect, url_for
import os

UPLOAD_FOLDER = '/path/to/upload/folder'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('upload_file', filename=filename))
    return '''
    <!doctype html>
    <title>Upload a File</title>
    <h1>Upload File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''
```
* The `/upload` route allows users to upload a file through a basic HTML form.
* The uploaded file is saved to a specified upload folder on the server.

### 15. Return JSON List of Users
```python
users = [{'id': 1, 'name': 'Alice'}, {'id': 2, 'name': 'Bob'}]

@app.route('/users')
def get_users():
    return jsonify(users)
```
* A static list `users` is defined, and a route `/users` returns this list in a JSON format.
* This is an example of how to serve JSON data of users in a RESTful API.

### 16. Flask App with Environment Variables
```python
import os
from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'default-secret-key')

@app.route('/')
def hello():
    return "Hello, World!"
```
* Configuration values like `SECRET_KEY` are fetched from environment variables.
* This approach boosts security and flexibility since sensitive or deployment-specific values aren’t hardcoded.

### 17. Rate-Limited Route
```python
from flask import Flask, request, jsonify
from flask_limiter import Limiter

app = Flask(__name__)
limiter = Limiter(app, key_func=get_remote_address)

@app.route('/limited', methods=["GET"])
@limiter.limit("5 per minute")
def limited():
    return jsonify(success=True), 200
```
* Using `flask_limiter`, the `/limited` route is rate-limited to 5 requests per minute.
* Further requests within the same minute receive a 429 status code (Too Many Requests).

### 18. Reverse String Route
```python
@app.route('/reverse')
def reverse_string():
    original = request.args.get('string', '')
    reversed_str = original[::-1]
    return reversed_str
```
* The `/reverse` route fetches a string query parameter, reverses it, and returns the result.
* For `/reverse?string=hello`, the response will be `olleh`.

### 19. Current Server Time in JSON
```python
import datetime

@app.route('/time')
def get_time():
    current_time = datetime.datetime.now().isoformat()
    return jsonify(time=current_time)
```
* The `/time` route retrieves the current server time using Python's `datetime` and returns it as a JSON object.

### 20. Serve a Static HTML File
```python
@app.route('/static-page')
def static_page():
    return app.send_static_file('page.html')
```
* A route that serves a static HTML file named `page.html` from the Flask app's `static` folder.
* Ideal for serving static content like HTML, CSS, and JS files without creating specific routes for each file.

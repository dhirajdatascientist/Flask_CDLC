# Flask program to create a RESTful API 

```python
from flask import Flask, jsonify

app = Flask(__name__)

# Sample data
data = {'message': 'Hello, World!'}

@app.route('/api', methods=['GET'])
def get_data():
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
```

In this example:

1. We import Flask and create a Flask web application.
2. We define a dictionary `data` which will be returned as JSON when someone accesses the `/api` endpoint.
3. We create a route `/api` using the `@app.route` decorator that listens for GET requests.
4. The `get_data` function is associated with this route and returns the `data` dictionary as JSON using Flask's `jsonify` method.
5. Finally, we run the Flask app with `app.run(debug=True)`.

You can run this code, and when you access `http://localhost:5000/api` in your web browser or through a tool like Postman, you'll receive the JSON response: `{"message": "Hello, World!"}`.

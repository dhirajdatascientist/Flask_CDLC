# Testing a API using Postman and Flask . 
* In this example, we'll create a Flask API that responds to GET and POST requests, and then we'll use Postman to test it.

**1. Install Flask:**

If you haven't already, you need to install Flask. You can do this using pip:

```bash
pip install flask
```

**2. Create a Simple Flask API:**

Create a Python file (e.g., `app.py`) and add the following code:

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# Define a simple dictionary to store data
data = {"message": "Hello, World!"}

@app.route('/', methods=['GET'])
def get_message():
    return jsonify(data)

@app.route('/', methods=['POST'])
def update_message():
    new_message = request.get_json()
    data['message'] = new_message.get('message', '')
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
```

This code creates a Flask application with two routes: one for GET requests to retrieve the message and one for POST requests to update the message.

**3. Run the Flask App:**

Run the Flask application by executing the following command in your terminal:

```bash
python app.py
```

Your Flask app should now be running locally at `http://localhost:5000`.

**4. Test the API with Postman:**

Now, you can use Postman to test your API.

- Open Postman.
- Create a new request.
- Set the request type to "GET" or "POST" depending on what you want to test.
- Enter the URL as `http://localhost:5000/`.
- If you're making a POST request, go to the "Body" tab and select "raw," then enter a JSON object like this:

```json
{
    "message": "New message from Postman"
}
```

- Click the "Send" button.

For a GET request, you should see the current message in the response body. For a POST request, you should see the updated message in the response.
# ADLC(L1)

1. How you can create a REST API in Python using Flask that responds with the message "Hello, Ram!" when a GET request is made to the "/api" endpoint?


* To create a REST API in Python using Flask that responds with the message "Hello, Ram!" when a GET request is made to the "/api" endpoint, you can follow these steps:

1. Install Flask: If you haven't already, you need to install Flask. You can do this using pip:

```
pip install Flask
```

2. Create a Python script for your Flask application. You can name it something like `app.py`. Here's an example of how to create a simple Flask API:

```python
from flask import Flask

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def hello_ram():
    return 'Hello, Ram!'

if __name__ == '__main__':
    app.run(debug=True)
```

In this script:

- We import the Flask class from the Flask library.
- We create an instance of the Flask class and name it `app`.
- We define a route for the "/api" endpoint using the `@app.route` decorator. It specifies that the `hello_ram` function should be executed when a GET request is made to "/api."
- The `hello_ram` function simply returns the string "Hello, Ram!" as the response.

3. Run your Flask application:

```
python app.py
```

Your Flask application should now be running, and you can access the API by making a GET request to the "/api" endpoint.

For example, if you're running the app locally, you can open a web browser or use a tool like `curl` to make a GET request:

```
curl http://localhost:5000/api
```

You should receive the response "Hello, Ram!" in your terminal or browser.
# Variable Route decorator 


```python
from flask import Flask

app = Flask(__name__)

@app.route('/book/<restaurant_id>', methods=['GET', 'POST'])
def book(restaurant_id):
    return f"Booking restaurant with ID: {restaurant_id}"

if __name__ == '__main__':
    app.run(debug=True)
```

In this example, when you access a URL like `/book/123`, Flask will capture the value `123` from the URL and pass it as the `restaurant_id` argument to the `book` function. The function then uses this value to generate a response. So, if you visit `/book/123`, you will see the response "Booking restaurant with ID: 123" in your browser.
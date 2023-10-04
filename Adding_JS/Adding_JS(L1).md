## To add JavaScript (JS) to your Flask application and link it to your HTML template, follow these steps:

1. Create a JavaScript File:

In the same directory as your `app.py` file, create a folder named `static` if you haven't already. Inside the `static` folder, create a JavaScript file named `script.js`. This is where you'll define your JavaScript code.

For example, let's create a simple script to display an alert when a button is clicked:

```javascript
// static/script.js
document.addEventListener("DOMContentLoaded", function () {
    var button = document.getElementById("myButton");
    button.addEventListener("click", function () {
        alert("Button Clicked!");
    });
});
```

2. Link the JavaScript File to Your HTML Template:

Open your `hello.html` template (located in the `templates` folder) and add a reference to your JavaScript file just before the closing `</body>` tag:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Hello, World!</title>
    <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <h1>Hello, World!</h1>

    <button id="myButton">Click Me</button>

    <script src="{{ url_for('static', filename='script.js') }}"></script>
</body>
</html>
```

Here, we use the `url_for` function to generate a URL for the `script.js` file, which is located in the `static` folder. We also added a button with the `id` "myButton" to demonstrate the JavaScript functionality.

3. Restart the Flask Application:

If your Flask application is still running, stop it (press Ctrl+C in the terminal) and restart it:

```
python app.py
```

4. Access the Application:

Visit http://localhost:5000/ in your web browser. Now, when you click the "Click Me" button, you should see an alert with the message "Button Clicked!"

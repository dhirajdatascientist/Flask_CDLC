# To Add CSS to your Flask application 

1. Create a CSS File:

In the same directory as your `app.py` file, create a folder named `static`. Inside the `static` folder, create a CSS file named `style.css`. This is where you'll define your CSS styles.

For example, let's create a simple style to change the color and center the text:

```css
/* static/style.css */
body {
    text-align: center;
    background-color: #f0f0f0;
}

h1 {
    color: #333;
}
```

2. Link the CSS File to Your HTML Template:

Open your `hello.html` template (located in the `templates` folder) and add a link to your CSS file in the `<head>` section of the HTML:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Hello, World!</title>
    <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <h1>Hello, World!</h1>
</body>
</html>
```

**Explanation** 

* Here, we use the `url_for` function to generate a URL for the `style.css` file, which is located in the `static` folder. 
* This link will ensure that the CSS styles are applied to the HTML template.

3. Update Your Flask Application to Serve Static Files:

In your `app.py` file, add the following line of code to configure Flask to serve static files (CSS, JavaScript, images, etc.):

```python
app = Flask(__name__, static_url_path='/static')
```

This line tells Flask to look for static files in the `/static` URL path.

4. Restart the Flask Application:

If your Flask application is still running, stop it (press Ctrl+C in the terminal) and restart it:

```
python app.py
```

5. Access the Application:

Visit http://localhost:5000/ in your web browser again, and now you should see the "Hello, World!" message with the CSS styles applied.


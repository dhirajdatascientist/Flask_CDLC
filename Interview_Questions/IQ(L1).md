```
1. What is Flask?
Flask is a micro web framework for Python used to build web applications. It is simple and lightweight and follows the WSGI standard.

2. How do you install Flask?
You can install Flask using pip, the Python package manager, by running `pip install Flask`.

3. What is the difference between Flask and Django?
Flask is a micro framework that provides flexibility and requires you to choose components, while Django is a full-stack framework with many built-in features and conventions.

4. How do you create a Flask application?
To create a Flask application, you typically create a Python file, define routes and views, and run the app using `app.run()`.

5. What is a Flask route?
A Flask route is a URL endpoint that maps to a specific view or function in your application.

6. How do you define a route in Flask?
You can define a route in Flask using the `@app.route` decorator above a function that handles the route.

7. What is the purpose of the `__name__` variable in Flask?
The `__name__` variable is used to determine whether the Python script is being run as the main program or imported as a module. It's often used to start the Flask application.

8. What is a Flask view function?
A Flask view function is a Python function that handles a specific route and returns a response to the client.

9. How do you create a simple "Hello, World!" Flask application?

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()


10. What is Jinja2, and how is it used in Flask?
Jinja2 is a template engine for Python used in Flask to render dynamic HTML templates. It allows you to insert dynamic content into HTML templates.

11. How do you render an HTML template in Flask using Jinja2?
You can render an HTML template using `render_template` from Flask and passing the template file name and any data you want to pass to the template.

12. What is the purpose of the `request` object in Flask?
The `request` object in Flask contains information about the incoming HTTP request, including data, headers, and form inputs.

13. What is the purpose of the `session` object in Flask?
The `session` object in Flask allows you to store user-specific data that persists across multiple requests.

14. How do you access form data submitted via POST requests in Flask?
You can access form data from POST requests using `request.form` in Flask.

15. What is a Flask extension?
A Flask extension is a package that adds extra functionality to Flask. Examples include Flask-SQLAlchemy and Flask-WTF.

16. How do you create a database connection in Flask?
You can create a database connection in Flask using extensions like Flask-SQLAlchemy or Flask-SQL.

17. What is Flask-WTF, and what is its purpose?
Flask-WTF is a Flask extension that simplifies working with web forms. It provides features for form validation and security.

18. How do you handle authentication in a Flask application?
Authentication in Flask can be handled using Flask-Login or similar extensions. You typically implement custom authentication logic.

19. Explain how Flask handles URL routing and variable routing.
Flask uses the `@app.route` decorator to define routes, and you can use angle brackets (`<>`) to create variable routes that capture values from the URL.

20. What is the purpose of the `url_for` function in Flask?
The `url_for` function in Flask is used to generate URLs for routes defined in the application, making it easier to avoid hardcoding URLs.

21. How do you handle errors in Flask?
Flask allows you to define error handlers using `@app.errorhandler` for specific HTTP error codes or exceptions.

22. What is Flask-SQLAlchemy, and how is it used?
Flask-SQLAlchemy is an extension for Flask that simplifies working with databases. It provides an Object-Relational Mapping (ORM) layer for database operations.

23. How do you create and migrate a database schema in Flask-SQLAlchemy?
You can create and migrate a database schema in Flask-SQLAlchemy by defining database models and using migration tools like Alembic.

24. Explain the purpose of Flask-Migrate.
Flask-Migrate is an extension that allows you to handle database schema migrations easily when using Flask-SQLAlchemy.

25. What is RESTful routing in Flask?
RESTful routing in Flask is a design pattern that maps HTTP methods (GET, POST, PUT, DELETE) to specific routes and views to create a RESTful API.

26. How do you set up authentication for a REST API in Flask?
Authentication for a REST API in Flask can be implemented using token-based authentication, OAuth2, or other authentication mechanisms.

27. What is Flask-CORS, and why is it used?
Flask-CORS is an extension that allows you to enable Cross-Origin Resource Sharing (CORS) in your Flask application, making it possible to request resources from a different domain.

28. How do you handle file uploads in Flask?
You can handle file uploads in Flask using the `request.files` object and save the uploaded files to a designated location on the server.

29. What is the purpose of Flask-RESTful, and how is it used?
Flask-RESTful is an extension that simplifies the creation of RESTful APIs in Flask by providing classes for creating resources, handling requests, and defining routes.

30. How do you handle middleware in Flask?
Flask allows you to use middleware functions or decorators to execute code before and after request processing.

31. What is Flask Blueprints, and why are they used?
Flask Blueprints are a way to organize routes and views into separate modules or packages, making it easier to structure large Flask applications.

32. What is the purpose of the `g` object in Flask, and how is it used?
The `g` object in Flask is a global context object that can be used to store and share data during a single request-response cycle.

33. How do you run a Flask application in production?
In production, you typically use a production-ready web server like Gunicorn or uWSGI to serve a Flask application behind a reverse proxy like Nginx or Apache.

34. Explain how to handle database transactions in Flask-SQLAlchemy.
Database transactions in Flask-SQLAlchemy are managed using the `db.session` object. You can use `db.session.commit()` to commit changes and `db.session.rollback()` to roll back changes in case of errors.

35. What is the purpose of Flask-JWT, and how is it used for token-based authentication?
Flask-JWT is an extension that simplifies token-based authentication in Flask applications. It provides decorators and functions for managing JWT (JSON Web Token) authentication.

36. How do you secure a Flask application against common security vulnerabilities?
You can secure a Flask application by following best

 practices such as input validation, using secure password storage, implementing proper session management, and protecting against CSRF attacks.

37. What is the difference between a Flask Blueprint and a Flask Extension?
A Flask Blueprint is a way to organize routes and views within a Flask application, while a Flask Extension is a third-party package that adds specific functionality to Flask.

38. What is WSGI, and how does Flask use it?
WSGI (Web Server Gateway Interface) is a standard for Python web applications. Flask uses WSGI to interface with web servers, making it compatible with various server implementations.

39. How do you set up and use Flask sessions to store user data?
You can set up Flask sessions by configuring the `SECRET_KEY` and using the `session` object to store and retrieve user data between requests.

40. What is the purpose of the `before_request` and `after_request` decorators in Flask?
The `before_request` decorator allows you to execute code before each request, and the `after_request` decorator allows you to modify the response after a request has been processed.

41. Explain the use of Flask-SocketIO in creating real-time web applications.
Flask-SocketIO is an extension that adds WebSocket support to Flask, allowing you to build real-time web applications with features like chat and live updates.

42. What is the significance of Flask's built-in development server?
Flask comes with a built-in development server that is convenient for development and testing but should not be used in production. It can be started using `app.run()`.

43. How do you handle database migrations in Flask?
Database migrations in Flask can be handled using extensions like Flask-Migrate and Alembic. These tools help manage changes to the database schema.

44. What is the purpose of Flask-Security, and how is it used for authentication and authorization?
Flask-Security is an extension for Flask that provides features for authentication and authorization, including user management, role-based access control, and more.

45. How do you handle authentication and authorization in a Flask application?
Authentication can be handled using extensions like Flask-Login or Flask-Security, and authorization can be implemented using custom decorators or role-based access control.

46. What is Flask-RESTPlus, and how is it used for building RESTful APIs?
Flask-RESTPlus is an extension that simplifies the creation of RESTful APIs in Flask by providing tools for documentation, validation, and request parsing.

47. How do you handle custom error pages in Flask?
You can handle custom error pages in Flask by defining error handlers for specific HTTP status codes using `@app.errorhandler`.

48. What is the purpose of the `flash` function in Flask, and how is it used?
The `flash` function in Flask is used to store a message that can be displayed to the user on the next request. It is commonly used for displaying success or error messages.

49. How do you handle database migrations in Flask-SQLAlchemy using Alembic?
You can use Alembic, a database migration tool, with Flask-SQLAlchemy to create and manage database schema migrations. Alembic generates migration scripts based on changes to your models.

50. What is the use of Flask-Login, and how is it used for user authentication?
Flask-Login is an extension that simplifies user authentication in Flask applications. It provides decorators and methods for handling user sessions and authentication.
```



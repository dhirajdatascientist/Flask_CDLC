MCQ - 1 Mark Each
COding Question - 5 Mark Each
Time limit : 1 HR.

# Multiple-choice questions (MCQs) on Flask and SQL
```
Flask Questions:

1. What is Flask?
   a) A database management system
   b) A micro web framework for Python
   c) A JavaScript library
   d) A text editor

2. Which of the following is not a Flask extension?
   a) Flask-SQLAlchemy
   b) Flask-RESTful
   c) Flask-HTML
   d) Flask-WTF

3. How can you create a new Flask application instance?
   a) app = Flask()
   b) app = Flask(__init__)
   c) app = Flask(__main__)
   d) app = Flask(__app__)

4. What HTTP method is typically used for retrieving data in Flask?
   a) POST
   b) PUT
   c) GET
   d) DELETE

5. Which template engine is commonly used with Flask for rendering HTML templates?
   a) Django Templates
   b) Jinja2
   c) Mustache
   d) Handlebars

6. How do you define a route in Flask using a decorator?
   a) @route('/')
   b) @app.route('/')
   c) @url('/')
   d) @path('/')

7. Which command is used to run a Flask application in debug mode?
   a) flask debug
   b) flask run --debug
   c) flask app --debug
   d) flask run --debugger

8. What is the purpose of the `request` object in Flask?
   a) To handle database queries
   b) To store application configuration
   c) To represent the HTTP request made to the application
   d) To define route patterns

9. How can you access query parameters in Flask?
   a) Using the `request` object's `params` attribute
   b) Using the `request` object's `form` attribute
   c) Using the `request` object's `query` attribute
   d) Using the `request` object's `args` attribute

10. What is the default port on which a Flask development server runs?
    a) 80
    b) 8080
    c) 5000
    d) 3000

SQL Questions:

11. What does SQL stand for?
    a) Structured Query Language
    b) Sequential Query Language
    c) Simple Query Language
    d) Standard Query Language

12. Which SQL statement is used to retrieve data from a database?
    a) UPDATE
    b) DELETE
    c) SELECT
    d) INSERT

13. Which clause is used to filter rows in an SQL SELECT statement?
    a) WHERE
    b) HAVING
    c) GROUP BY
    d) ORDER BY

14. Which SQL data type is used to store text with a maximum length?
    a) INT
    b) VARCHAR
    c) DATE
    d) BOOLEAN

15. What is the primary key in an SQL table?
    a) A key used to unlock the database
    b) A unique identifier for each row in the table
    c) The first column in the table
    d) A foreign key from another table

16. Which SQL statement is used to add new rows to a table?
    a) ALTER TABLE
    b) INSERT INTO
    c) UPDATE
    d) CREATE TABLE

17. What is an SQL JOIN used for?
    a) To create a new table
    b) To combine rows from two or more tables based on a related column
    c) To delete rows from a table
    d) To update existing rows in a table

18. Which SQL clause is used to sort the result set in ascending or descending order?
    a) GROUP BY
    b) ORDER BY
    c) HAVING
    d) WHERE

19. What is the purpose of the SQL GROUP BY clause?
    a) To delete duplicate rows in a table
    b) To filter rows based on a condition
    c) To group rows that have the same values in specified columns
    d) To update rows in a table

20. Which SQL statement is used to delete data from a database table?
    a) DELETE FROM
    b) DROP TABLE
    c) REMOVE FROM
    d) TRUNCATE TABLE

21. How do you create a route in Flask that accepts a dynamic parameter from the URL?
    a) @app.route('/user/<int:id>')
    b) @app.route('/user')
    c) @app.route('/user?id=<int>')
    d) @app.route('/user/<str>')

22. Which HTTP status code is typically used to indicate a successful response in Flask?
    a) 200 OK
    b) 404 Not Found
    c) 500 Internal Server Error
    d) 401 Unauthorized

23. In Flask, what does the `redirect` function do?
    a) Renders an HTML template
    b) Redirects the user to another URL
    c) Sends an HTTP POST request
    d) Retrieves data from a database

24. What is the purpose of Flask's `session` object?
    a) To store user session data between requests
    b) To define the structure of a database table
    c) To manage authentication and authorization
    d) To handle file uploads

25. Which command is used to install Flask using pip?
    a) pip install flask
    b) pip install flask-app
    c) pip install python-flask
    d) pip flask-install


26. Which SQL function is used to find the total number of rows in a table?
    a) COUNT(*)
    b) SUM()
    c) AVG()
    d) MAX()

27. In SQL, what is a foreign key used for?
    a) To ensure data is unique in a column
    b) To create a primary key in a table
    c) To establish a relationship between two tables
    d) To rename a column in a table

28. What does the SQL statement "SELECT DISTINCT" do?
    a) Selects only the first row in a table
    b) Selects all rows from a table
    c) Selects only distinct (unique) values from a column
    d) Selects the columns in a table in a random order

29. Which SQL operator is used to combine multiple conditions in a WHERE clause?
    a) OR
    b) AND
    c) NOT
    d) XOR

30. What is the purpose of the SQL statement "ALTER TABLE"?
    a) To add a new column to an existing table
    b) To delete an entire table
    c) To insert data into a table
    d) To update data in a table
```


# Coding questions


1. **Basic Flask Routing**:
   
   Write a Flask application that has three routes:
   - `/`: Displays a "Hello, World!" message.
   - `/about`: Displays an "About Us" message.
   - `/contact`: Displays a "Contact Us" message.

2. **User Input Handling**:

   Create a Flask application that takes a user's name as input through a form and displays a personalized greeting message. The form should be accessible at `/input` and should use the POST method to submit the data to another route.

3. **Database Integration**:

   Build a Flask application that connects to a SQLite database and displays a list of items retrieved from the database on a route `/items`. You should have at least two routes - one for displaying the list and one for adding new items to the database.

4. **Authentication**:

   Develop a simple authentication system using Flask. Create two routes: `/login` and `/dashboard`. Users should be able to log in with a username and password on the `/login` route. After successful login, they should be redirected to the `/dashboard` route, which should display a welcome message with the user's name.

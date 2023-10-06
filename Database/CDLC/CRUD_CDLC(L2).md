# CRUD_CDLC(L2)

1. Set up your Python environment:

   First, make sure you have Python installed on your system. You can download it from the official Python website (https://www.python.org/downloads/) if you haven't already.

   Install the required libraries for web development using Flask and SQLite3:

   ```bash
   pip install Flask
   ```

2. Create a Python script for your web application:

   Create a Python file (e.g., `app.py`) and import the necessary modules:

   ```python
   from flask import Flask, request, render_template
   import sqlite3
   ```

3. Initialize your Flask app:

   ```python
   app = Flask(__name__)
   ```

4. Create an HTML form:

   Create an HTML file (e.g., `form.html`) that contains the form to input data. This form should send a POST request to your Flask app:

   ```html
   <!DOCTYPE html>
   <html>
   <head>
       <title>Insert Data</title>
   </head>
   <body>
       <form method="POST" action="/insert">
           <label for="id">ID:</label>
           
           <input type="text" name="id"><br><br>
           <label for="username">Username:</label>
           
           <input type="text" name="username"><br><br>
           <label for="email">Email:</label>
           
           <input type="text" name="email"><br><br>
           <input type="submit" value="Submit">
       </form>
   </body>
   </html>
   ```

5. Create a function to insert data into SQLite:

   In your `app.py` script, define a function to insert data into the SQLite database:

   ```python
   def insert_data(id, username, email):
       conn = sqlite3.connect('infy.db')
       cursor = conn.cursor()
       cursor.execute("INSERT INTO emp(id, username, email) VALUES (?, ?, ?)", (id, username, email))
       conn.commit()
       conn.close()
   ```

6. Define routes in your Flask app:

   Create routes for rendering the form and processing form submissions in your `app.py`:

   ```python
   @app.route('/')
   def show_form():
       return render_template('form.html')

   @app.route('/insert', methods=['POST'])
   def insert():
       id = request.form['id']
       username = request.form['username']
       email = request.form['email']
       insert_data(id, username, email)
       return "Data inserted successfully!"
   ```

7. Run your Flask app:

   In your terminal, navigate to the directory containing your `app.py` file and run the following command:

   ```bash
   python app.py
   ```

Your Flask app should now be running. Visit `http://localhost:5000` in your web browser to access the form and submit data. The data will be inserted into your SQLite database when you submit the form.
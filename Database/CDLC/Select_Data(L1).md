```python
@app.route('/')
def index():
    # Fetch all data from the database
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM emp")
    data = cursor.fetchall()
    conn.close()
    
    # Pass the data to an HTML template
    return render_template('index.html', data=data)
```
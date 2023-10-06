```python
from flask import Flask, render_template
import sqlite3

app = Flask(name)

@app.route('/')
def hello():
    return render_template('hello.html')

def connection():
    conn=sqlite3.connect('infy.db')
    return conn

def create_table():
    conn=connection()
    cursor = conn.cursor()

    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS emp(id INTEGER,username TEXT,email TEXT)
""")
    conn.commit()
    conn.close()

def insert_table():
    conn=connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO emp(id,username,email) VALUES (?,?,?)",("101","Sahil","sahil@gmail.com"))
    conn.commit()
    conn.close()

def delete():
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM emp WHERE id=?",(101,))
    conn.commit()
    conn.close()

def update():
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE emp SET username=? WHERE id=?",("ram",101))
    conn.commit()
    conn.close()

if name == 'main':
    connection()
    create_table()
    insert_table()
    update()
    app.run(debug=True)
```
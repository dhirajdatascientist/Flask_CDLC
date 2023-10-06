from flask import Flask, render_template,request
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/form')
def form():
    return render_template('form.html')

def create_table():
    conn = sqlite3.connect('infy.db')
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS emp(id INTEGER,username TEXT,email TEXT)
""")
    conn.commit()
    conn.close()

def insert_data(id, username, email):
    create_table()
    conn = sqlite3.connect('infy.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO emp(id, username, email) VALUES (?, ?, ?)", (id, username, email))
    conn.commit()
    conn.close()

@app.route('/add',methods=['POST'])
def add():
    id = request.form['id']
    username = request.form['username']
    email = request.form['email']
    insert_data(id, username, email)
    return render_template('form.html')

@app.route('/display')
def display():
    return render_template('display.html')

if __name__ == '__main__':
    app.run(debug=True)
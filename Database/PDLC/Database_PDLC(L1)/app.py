from flask import Flask, render_template
import sqlite3

app = Flask(__name__,static_url_path='/static')

@app.route('/home')
def home():
    create_table()
    insert_table()
    cname = "India"
    p1="Home"
    p2="Contact"
    p3="Services"
    paragraph = "Welcome to Flask World !!"
    return render_template('home.html',cname=cname,p1=p1,p2=p2,p3=p3,paragraph=paragraph)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/service')
def service():
    return render_template('service.html')


def create_table():
    conn = sqlite3.connect('infy.db')
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS emp(
                   id INTEGER,
                   username TEXT,
                   email TEXT

    )
""")
    conn.commit()
    conn.close()


def insert_table():
    conn = sqlite3.connect('infy.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO emp(id,username,email) VALUES (?,?,?)",("101","Sahil","sahil@gmail.com"))
    conn.commit()
    conn.close()

app.run(debug=True)
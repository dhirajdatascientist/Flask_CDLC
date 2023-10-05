from flask import Flask, render_template

app = Flask(__name__,static_url_path='/static')

@app.route('/home')
def home():
    cname = "India"
    p1="Home"
    p2="Contact"
    p3="Services"
    return render_template('home.html',cname=cname,p1=p1,p2=p2,p3=p3)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/service')
def service():
    return render_template('service.html')

app.run(debug=True)
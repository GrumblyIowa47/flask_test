
from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)

@app.route("/")

def index():
    return "Index page"

@app.route("/hello")
@app.route("/hello/")
@app.route("/hello/<name>")

def hello(name=None):
    return render_template('home.html', user=name)  

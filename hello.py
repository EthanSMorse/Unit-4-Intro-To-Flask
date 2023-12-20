from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index ():
    return render_template("home.html.jinja")

@app.route('/ping')
def ping ():
    return("pong")

@app.route('/hello/<name>')
def hello(name):
    return f"Hello, {name}"
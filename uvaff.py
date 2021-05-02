from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home_C.html")



@app.route('/signin')
def signin():
    return render_template("signin.html")


@app.route('/signup')
def signup():
    return render_template("signup.html")


@app.route('/signup/competitor')
def create_competitor():
    return render_template("competitor.html")


@app.route('/signup/host')
def create_host():
    return render_template("host.html")
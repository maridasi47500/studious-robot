from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("hey.html")

@app.route("/signup")
def inscription():
    return render_template("signup.html")

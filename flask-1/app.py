from flask import Flask, session, render_template, request, jsonify, flash

app = Flask(__name__)
app.config["SECRET_KEY"] = "SecRETKey"

@app.route("/")
def home_page():
    return render_template("home.html")


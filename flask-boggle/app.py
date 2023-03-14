from boggle import Boggle
from flask import Flask, render_template, session
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config["SECRET_KEY"] = "SecRETKey"
boggle_game = Boggle()
debug = DebugToolbarExtension(app)

def initialize_board():
    if not session.get("board"):
        board = boggle_game.make_board()
        session["board"] = board

@app.route("/home")
def home_page():
    initialize_board()
    return(render_template("home.html", board=session["board"]))

def main():
    initialize_board()

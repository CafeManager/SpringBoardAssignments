from boggle import Boggle
from flask import Flask, render_template, session, request, jsonify
from flask_debugtoolbar import DebugToolbarExtension
import os


app = Flask(__name__)
app.config["SECRET_KEY"] = "SecRETKey"
boggle_game = Boggle()
debug = DebugToolbarExtension(app)

word_list = []



def initialize_word_list():
    # from https://towardsthecloud.com/get-relative-path-python
    # This opens files using relative filepath as opposed to writing the absolute path
    absolute_path = os.path.dirname(__file__)
    relative_path = "words.txt"
    full_path = os.path.join(absolute_path, relative_path)
    print(full_path)
    file = open(full_path, "r")
    return file

def initialize_board():
    if not session.get("board"):
        board = boggle_game.make_board()
        session["board"] = board
    #     word_list = initialize_word_list()
    #     print(word_list)
    # print(word_list)

    

def check_if_in_words(word):
    file = initialize_word_list()
    for line in file:
        if word == line.strip():
            return {"result":"ok"}
    return {"result": "not-on-board"}

@app.route("/home")
def home_page():
    initialize_board()
    return(render_template("home.html", board=session["board"]))

@app.route("/guess", methods=["POST"])
def process_guess():

    guess = request.get_json()["guess"]
    check = check_if_in_words(guess)    
    check = jsonify(check)
    # print(check)
    # import pdb
    # pdb.set_trace()
    # session["result"] = check
    return check

def main():
    initialize_board()

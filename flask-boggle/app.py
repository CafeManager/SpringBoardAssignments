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
        session["score"] = 0
        if not session.get("past_scores"):
            session["past_scores"] = []


def check_if_in_words(word):
    result =  boggle_game.check_valid_word(session["board"], word)
    print(result)
    return result

@app.route("/")
def home_page():
    initialize_board()
    return(render_template("home.html", board=session["board"]))

@app.route("/guess", methods=["POST"])
def process_guess():
    #adds score
    guess = request.get_json()["guess"]
    check = check_if_in_words(guess)   
    if str(check).strip() == "ok":       
        session["score"] = session["score"] + len(guess)
    check = jsonify(check.strip())
    return check

@app.route("/sendResult", methods=["POST"])
def process_game_results():
    # resets session variables for next instance and adds past score
    results = request.get_json() 
    newList = session["past_scores"]
    newList.append(results["result"])
    session["past_scores"] = newList
    session["score"] = 0
    session["board"] = []
    
    return jsonify(newList)

def main():
    initialize_board()

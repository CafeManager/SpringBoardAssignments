from flask import Flask, render_template, redirect, request, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey

app = Flask(__name__)
app.config["SECRET_KEY"]= "hi"



debug = DebugToolbarExtension(app)
@app.route("/")
def home():
    return render_template("home.html", title=satisfaction_survey.title, instructions=satisfaction_survey.instructions)

# This is an extra layer of routing. Is this necessary?        
@app.route("/question/")
def question_load():   
    if not session["responses"]:
        session["responses"] = []
    return redirect("/question/1")

@app.route("/question/<int:id>")
def question(id):
    responses = session["responses"]
    curr_question_ID = id -1 
    next_question_ID_from_responses = len(responses) + 1
    if curr_question_ID != next_question_ID_from_responses-1:
        flash("Invalid URL Link. Redirected to next question in survey.")
        redirectString = "/question/" + str(next_question_ID_from_responses)
        return redirect(redirectString)
    if curr_question_ID >= len(satisfaction_survey.questions):
        flash("All questions already submitted. Redirected to end page.")
        return redirect("/results")
    
    return render_template("question.html", \
                           test=responses, \
                            question=satisfaction_survey.questions[curr_question_ID].question, \
                            choices=satisfaction_survey.questions[curr_question_ID].choices, \
                            id = id)

@app.route("/answer", methods=["POST"])
def answer():
    # id = request.form["id"]
    responses = session["responses"]
    current_question_ID_from_responses = len(responses) + 1
    next_question_ID_from_responses = len(responses) + 2
    if "answer" in request.form.keys():
        nextId = len(responses) + 1
        responses.append((current_question_ID_from_responses, request.form["answer"]))
        session["responses"] = responses
        
    if(len(responses) == len(satisfaction_survey.questions)):
        return redirect("/results")
    #return redirect("question.html", test=responses, question=satisfaction_survey.questions[nextId].question, choices=satisfaction_survey.questions[nextId].choices, id = nextId)
    redirectString = "/question/" + str(next_question_ID_from_responses)
    return redirect(redirectString)

@app.route("/results")
def results():
    responses = session["responses"]
    if len(responses) < len(satisfaction_survey.questions):
        flash("Not all questions answered yet. Redirected to next question to be answered.")
        current_question_ID_from_responses = len(responses) + 1
        redirectString = "/question/" + str(current_question_ID_from_responses)
        return redirect(redirectString)
    return render_template("results.html", results=responses)
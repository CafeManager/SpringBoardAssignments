from flask import Flask, render_template, request 
from flask_debugtoolbar import DebugToolbarExtension
from stories import story


app = Flask(__name__)
app.config['SECRET_KEY'] = "hi"

debug = DebugToolbarExtension(app)
@app.route('/form')
def home_page():    
    return render_template('form.html', prompts=story.prompts)

@app.route('/generate')
def generate():
    generated = {}
    for x in request.args:
        generated[x] = request.args[x]
    generatedStory = story.generate(generated)
    return render_template('story.html', story = generatedStory)
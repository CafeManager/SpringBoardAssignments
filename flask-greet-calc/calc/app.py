# Put your app in here.
from flask import request, Flask 

app = Flask(__name__)

@app.route('/add')
def add_route():
    parsedA, parsedB = int(request.args["a"]) , int(request.args["b"])
    total = add(parsedA, parsedB)
    return f'{total}'    

@app.route('/sub')
def sub_route():
    parsedA, parsedB = int(request.args["a"]) , int(request.args["b"])
    total = sub(parsedA, parsedB)
    return f'{total}'    

@app.route('/mult')
def mult_route():
    parsedA, parsedB = int(request.args["a"]) , int(request.args["b"])
    total = mult(parsedA, parsedB)
    return f'{total}'    

@app.route('/div')
def div_route():
    parsedA, parsedB = int(request.args["a"]) , int(request.args["b"])
    total = div(parsedA, parsedB)
    return f'{total}'    

@app.route('/math/<operation>')
def operationHandler(operation):
    parsedA, parsedB = int(request.args["a"]) , int(request.args["b"])
    total = eval(operation)(parsedA, parsedB)
    return f'{total}'


"""Basic math operations."""

def add(a, b):
    """Add a and b."""
    
    return a + b

def sub(a, b):
    """Substract b from a."""

    return a - b

def mult(a, b):
    """Multiply a and b."""

    return a * b

def div(a, b):
    """Divide a by b."""

    return a / b
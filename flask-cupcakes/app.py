"""Flask app for Cupcakes"""
from flask import Flask, jsonify, request, render_template, flash, redirect
from flask_debugtoolbar import DebugToolbarExtension
from models import connect_db, Cupcake, db


app = Flask(__name__)
app.config["SECRET_KEY"] = 'do-not-share32'
debug = DebugToolbarExtension(app)
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql:///cupcake'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True

connect_db(app)

@app.route('/')
def get_homepage():
    cupcakes = Cupcake.query.all()
    return render_template('homepage.html', cupcakes=cupcakes)

@app.route('/api/cupcakes')
def get_all_cupcakes():
    cupcakes = Cupcake.query.all()
    serialized_cupcakes = [cupcake.serialize() for cupcake in cupcakes]
    return jsonify(cupcakes=serialized_cupcakes)

@app.route('/api/cupcakes/<int:id>')
def get_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)
    return jsonify(cupcake=cupcake.serialize())

@app.route('/api/cupcakes', methods=['POST'])
def add_cupcake():
    
    flavor = request.json.get("flavor")
    size = request.json.get("size")
    rating = request.json.get("rating")
    image = request.json.get("image")
    attr_dict = {
        'flavor': flavor,
        'size': size,
        'rating': rating
    }

    try:
        if image:
            cupcake =  Cupcake(**attr_dict, image=image)
        else:
            cupcake = Cupcake(**attr_dict)
        db.session.add(cupcake)
        db.session.commit()

    except:
        flash("Failed to add Cupcake", "error")
        return (jsonify(message="Invalid Cupcake Data"), 400)
    
    flash("Added cupcake", "info")
    return (jsonify(cupcake=cupcake.serialize()), 201)

# Criticism Note: Enter added for readability sake. Is there a better way to space it?
@app.route('/api/cupcakes/<int:id>', methods=['PATCH'])
def patch_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)

    cupcake.flavor = request.json.get("flavor", cupcake.flavor)
    cupcake.size = request.json.get("size", cupcake.size)
    cupcake.rating = request.json.get("rating", cupcake.rating)
    cupcake.image = request.json.get("image", cupcake.image)
    
    db.session.add(cupcake)
    db.session.commit()
    return jsonify(cupcake=cupcake.serialize())

@app.route('/api/cupcakes/<int:id>', methods=['DELETE'])
def delete_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)
    db.session.delete(cupcake)
    db.session.commit()
    return jsonify(message="Deleted")







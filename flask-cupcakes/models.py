"""Models for Cupcake app."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)
    with app.app_context():
        db.create_all()

# id - pk
# flavor - not null text
# size -  not null text
# rating  - not null float
# image - not null text default https://tinyurl.com/demo-cupcake

class Cupcake(db.Model):
    def __repr__(self):
        cupcake = self
        return f"<Cupcake id={cupcake.id} flavor={cupcake.flavor} size={cupcake.size} rating={cupcake.rating}>"

    id = db.Column(db.Integer, primary_key=True,
                   autoincrement=True)
    
    flavor = db.Column(db.Text, nullable=False)

    size = db.Column(db.Text, nullable=False)

    rating = db.Column(db.Float, nullable=False)

    image = db.Column(db.Text, default="https://tinyurl.com/demo-cupcake")

    def serialize(self):
        return {
            'id': self.id,
            'flavor': self.flavor,
            'size': self.size,
            'rating': self.rating,
            'image': self.image
        }

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Apartment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    bhk = db.Column(db.String(10))
    price = db.Column(db.Integer)
    image = db.Column(db.String(300))





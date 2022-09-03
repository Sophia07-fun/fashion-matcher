from flask_sqlalchemy import SQLAlchemy
from app import app
from dataclasses import dataclass

db = SQLAlchemy(app)

@dataclass
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(40), unique=True, nullable=False)
    preferences = db.Column(db.String(6), nullable=True)
    password = db.Column(db.String(250), nullable=False)
    clothes = db.relationship('Clothing', backref='user', lazy=True)

    def __repr__(self):
        return '<User %r>' % self.email

class Clothing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    color = db.Column(db.String(12), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return '<Clothing %r>' % self.name

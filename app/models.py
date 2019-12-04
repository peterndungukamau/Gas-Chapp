from . import db


class Admin(db.Model):
    __tablename__ = 'admins'
    
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String, unique=True)
    password = db.column(db.String)
    
    
from . import db

class Cart(db.Model):
    '''Cart model'''
    
    __tablename__ = 'carts'
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(25), nullable=False)
    price = db.Column(db.String(), nullable=False)
    
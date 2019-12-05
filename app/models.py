from . import db
from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash
from . import login_manager
from datetime import datetime


@login_manager.user_loader

def load_user(user_id):
      
  '''
  function that queries the database to check if user exists
  '''
  return User.query.get(int(user_id))


class User(UserMixin,db.Model):
       
  '''
  class defining the table holding users data
  '''
  __tablename__='users'

  id=db.Column(db.Integer, primary_key=True)
  username=db.Column(db.String(255),index=True)
  email=db.Column(db.String(255), unique=True,index=True)
  pass_secure=db.Column(db.String())
  bio=db.Column(db.String(255))
  
  

  @property
  def password(self):
    '''
    function that raises an attribute error when someone tries to access the password field
    '''
    raise AttributeError('You have no access to passwords')

  @password.setter
  def password(self,password):
    '''
    function that generates hashes for a password then stores it in the db.
    '''
    self.pass_secure=generate_password_hash(password)

  def verify_password(self,password):
    '''
    function that check the hashed password in db and the login password if the are same
    '''
    return check_password_hash(self.pass_secure,password)

  def __repr__(self):
    '''
    function that helps in debugging.
    '''
    return f'User {self.username}'


class Vendor(UserMixin,db.Model):
    __tablename__ = 'vendor'
    
    id = db.Column(db.Integer,primary_key = True)
    username=db.Column(db.String(255),index=True)
    email=db.Column(db.String(255), unique=True,index=True)
    pass_word=db.Column(db.String())
    bio=db.Column(db.String(255))
    profile_pic_path=db.Column(db.String())
    location=db.Column(db.String)
    
    @property
    def password(self):
        '''
        function that raises an attribute error when someone tries to access the password field
        '''
        raise AttributeError('You have no access to passwords')

    @password.setter
    def password(self,password):
        '''
        function that generates hashes for a password then stores it in the db.
        '''
        self.pass_word=generate_password_hash(password)

    def verify_password(self,password):
          
        '''
        function that check the hashed password in db and the login password if the are same
        '''
        return check_password_hash(self.pass_word,password)
    
    def __repr__(self):
          return f'Vendor{self.username}'
        
@login_manager.user_loader

def load_user(user_id):
      
  '''
  function that queries the database to check if user exists
  '''
  return Vendor.query.get(int(user_id))

      
    
    
    
    
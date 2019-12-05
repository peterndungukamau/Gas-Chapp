from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,ValidationError,BooleanField,SelectField
from wtforms.validators import Required,Email,EqualTo
from ..models import Vendor


class Signup_vendorForm(FlaskForm):
    '''
    class defining how the sign up form looks like
    '''
    username=StringField('Enter Username',validators=[Required()])
    email=StringField('Enter your email address',validators=[Required(),Email()])
    location=SelectField(u'Enter Location', choices =[('Jahmuhuri','Jahmuhuri'),('Riara','Riara'),('Kilimani','Kilimani'),('Ayany','Ayany'),('Olympic','Olympic'),('Kenyatta','Kenyatta')])

    password=PasswordField('Enter a password', validators=[Required(),EqualTo('password_auth',message='Passwords must match')])
    password_auth=PasswordField('Confirm Password', validators=[Required()])
    submit=SubmitField('Sign Up!')

    def validate_email(self,data_field):
        '''
        function that validates no email duplicates
        '''
        if Vendor.query.filter_by(email=data_field.data).first():
            
            raise ValidationError('That Email is taken.Please use another email')

    def validate_username(self,data_field):
        '''
        function that validates no username duplicates
        '''
        if Vendor.query.filter_by(username=data_field.data).first():
            raise ValidationError('That username is taken.Try another name')
        
class Signin_vendorForm(FlaskForm):
        
    '''
    class defining how the sign in form looks like
    '''
    username=StringField('Enter your username', validators=[Required()])
    password=PasswordField('Enter your password', validators=[Required()])
    remember=BooleanField('Remember Me')
    submit=SubmitField('Log in!')
        
    
    
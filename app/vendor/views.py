from flask import render_template,url_for,request,flash,redirect
from . import vendor
from .. import db
from ..models import Vendor
from .forms import Signin_vendorForm,Signup_vendorForm
from flask_login import login_user,logout_user,login_required,current_user



@vendor.route('/register', methods=['GET','POST'])
def register():
    '''
    view function that renders sign up page to allow new users in the app
    '''
    form = Signup_vendorForm()

    if form.validate_on_submit():    
        user = Vendor(username=form.username.data,email=form.email.data,location=form.location.data,password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(f' vendor Account created for {form.username.data}! You are now able to log in ')
        return redirect(url_for('vendor.login'))

    return render_template('vendor/register.html',form = form)

@vendor.route('/login',methods=['GET','POST'])
def login():
    '''
    view function that renders the sign in for when called
    '''
    form = Signin_vendorForm()

    if form.validate_on_submit():
            user=Vendor.query.filter_by(username=form.username.data).first()

            if user is not None and user.verify_password(form.password.data):
                login_user(user,form.remember.data)
                return redirect(request.args.get('next') or url_for('main.index'))
            flash('invalidusername')
        
    return render_template('vendor/login.html',form=form)   

@vendor.route('/signout')  
@login_required
def signout():
    
    '''
    view function that logs out a user once called
    '''
    logout_user()
    return render_template('index.html')
 








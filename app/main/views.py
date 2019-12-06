from flask import render_template,request,redirect,url_for,abort, flash
from flask_login import login_required,current_user
from ..models import Vendor
from .forms import UpdateProfile, LocationForm
from .. import db
from . import main

orders = [
    {
        'img' : 'img',
        'vendor' : 'k-gas',
        'location' : '3200',
        'Price' : '3200',


    },

        {
        'img' : 'img',
        'vendor' : 'k-gas',
        'location' : '3200',
        'Price' : '3200',

    }
]

@main.route('/')
def index():
    
    return render_template('index.html',current_user=current_user)


@main.route('/user/<uname>')
def profile(uname):
    user = Vendor.query.filter_by(username = uname).first()

    if user is None:
        abort(404)
    postlist = Vendor.get_post(user.username)
    return render_template("profile/profile.html", user = user, postlist=postlist)


@main.route('/user/<uname>/update',methods = ['GET','POST'])
def update_profile(uname):
    user = Vendor.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()
        flash('Your account has been updated!')

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)
  
@main.route('/order')
def order():
    title = 'Gas-Chapp'
    return render_template('order.html', title=title, orders=orders)



@main.route('/location',methods=['GET','POST'])
def location():
    form = LocationForm()
    if form.validate_on_submit():
        flash(f'Thanks for Buying The gas will be delivered to {form.location.data} in 5 minutes!', 'success')
        return redirect(url_for('main.index'))
    return render_template('buy.html', form=form)
  


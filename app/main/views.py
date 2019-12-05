from . import main
from flask import render_template,request,redirect,url_for,abort
from flask_login import login_required,current_user
from ..models import Vendor
from .forms import UpdateProfile
from .. import db

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


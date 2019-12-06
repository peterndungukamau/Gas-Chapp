from . import main
from flask import render_template,flash,redirect,url_for
from .forms import LocationForm


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
    title = 'Gas-Chapp'
    return render_template('index.html', title=title,)

@main.route('/order')
def order():
    title = 'Gas-Chapp'
    return render_template('order.html', title=title, orders=orders)



@main.route('/location',methods=['GET','POST'])
def location():
    form = LocationForm()
    if form.validate_on_submit():
        flash(f'Thanks for Buying The gas will be delivered to {form.location.data}!', 'success')
        return redirect(url_for('main.order'))
    return render_template('buy.html', form=form)
  


    


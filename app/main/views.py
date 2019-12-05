from . import main
from flask import render_template


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




    


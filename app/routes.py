from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Michael'}
    stocks = [
        {
            'ticker': 'BYND',
            'price': 152.03,
            'currency': 'USD'
        },
        {
            'ticker': 'GME',
            'price': 1000.00,
            'currency': 'USD'
        },
        {
            'ticker': 'BB',
            'price': 14.86,
            'currency': 'CAD'
        }
    ]

    return render_template('index.html', title='Michael\'s Watchlist', user=user, stocks=stocks)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data
        ))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
from app import app
from app.models import User
from flask import render_template, flash, redirect, url_for, request
from app.forms import LoginForm
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse

@app.route('/')
@app.route('/index')
@login_required
def index():
    watchlist = [
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

    return render_template('index.html', title='Michael\'s Watchlist', watchlist=watchlist)

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Checks to see if the current user is logged in, and if so redirects to the index page
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()

    # Goes through the login process with the user
    if form.validate_on_submit():
        # Load the user's info from the database
        user = User.query.filter_by(username=form.username.data).first()

        # Checks if the password is valid
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        
        # Logs the user in using the submitted credentials
        login_user(user, remember=form.remember_me.data)

        # Routes the user to the original page they navigated to, after a successful login
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)

    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
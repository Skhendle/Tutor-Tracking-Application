from app import db
from flask import render_template, url_for, flash, redirect, request
from app.auth.forms import LoginForm
from flask_login import current_user,login_user,logout_user, login_required
from app.models import User
from werkzeug.urls import url_parse

from app.auth import auth



@auth.route('/welcome-page')
def index():
    return render_template('auth/index.html', title='index')

@auth.route('/', methods=['GET','POST'])
@auth.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():# pragma: no cover
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('auth.login'))
        login_user(user)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('auth.index')
        return redirect(next_page)
    return render_template('auth/login.html', title='Sign In', form=form)

@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/account_type')
def account_type():
    return render_template('auth/account_type.html',title='account type')



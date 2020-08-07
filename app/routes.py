from app import app, db
from flask import render_template, url_for, flash, redirect, request
from app.forms import LoginForm, LectureRegForm, TutorRegForm
from flask_login import current_user, login_user, logout_user , login_required
from app.models import User, Lecture ,Tutor
from werkzeug.urls import url_parse

@app.route('/')
@login_required
def index():
    return render_template('index.html', title='index')

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('auth/login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/account_type', methods=['GET','POST'])
def account_type():
    return render_template('account_type.html',title='account type')

@app.route('/tutor/registration', methods=['GET','POST'])
def tutorRegistration():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = TutorRegForm()
    if form.validate_on_submit():
        print('true')
        user = User(firstname=form.firstname.data,lastname=form.lastname.data, email=form.email.data,username=form.username.data)
        user.set_password(form.password1.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('auth/tutor_reg.html',title='tutor registation',form=form)

@app.route('/lecture/registration', methods=['GET','POST'])
def lectureRegistration():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LectureRegForm()
    if form.validate_on_submit():
        user = User(firstname=form.firstname.data,lastname=form.lastname.data, email=form.email.data,username=form.username.data)
        user.set_password(form.password1.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('auth/lecture_reg.html',title='lecture registation',form=form)

@app.route('/lecture_home')
def lecture_home():
    return render_template('lecture_home.html')

@app.route('/tutor_home')
def tutor_home():
    return render_template('tutor_home.html')
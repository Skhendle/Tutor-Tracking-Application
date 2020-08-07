from app import app
from flask import render_template, url_for
from app.forms import LoginForm, LectureRegForm, TutorRegForm

@app.route('/')
def index():
    return render_template('index.html', title='index')

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    return render_template('auth/login.html',title='login',form=form)

@app.route('/account_type', methods=['GET','POST'])
def account_type():
    return render_template('account_type.html',title='account type')

@app.route('/tutor/registration', methods=['GET','POST'])
def tutorRegistration():
    form = TutorRegForm()
    return render_template('auth/tutor_reg.html',title='tutor registation',form=form)

@app.route('/lecture/registration', methods=['GET','POST'])
def lectureRegistration():
    form = LectureRegForm()
    return render_template('auth/lecture_reg.html',title='lecture registation',form=form)
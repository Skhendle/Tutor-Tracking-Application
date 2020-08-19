from app import app, db
from flask import render_template, url_for, flash, redirect, request
from app.forms import LoginForm, LectureRegForm, TutorRegForm , EditTutorProfileForm, EditLectureProfileForm, StudentRegForm
from flask_login import current_user, login_user, logout_user , login_required
from app.models import User, Lecture ,Tutor, Student
from werkzeug.urls import url_parse


@app.route('/')
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


@app.route('/account_type')
def account_type():
    return render_template('account_type.html',title='account type')

@app.route('/tutor/profile')
@login_required
def tutor_profile():
    return render_template('tutor_profile.html',title='profile')

@app.route('/student/profile')
@login_required
def student_profile():
    return render_template('student_profile.html',title='profile')

@app.route('/lecture/profile')
@login_required
def lecture_profile():
    return render_template('lecture_profile.html',title='profile')


@app.route('/student/registration', methods=['GET','POST'])
def studentRegistration():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = StudentRegForm()
    if form.validate_on_submit():
        user = User(firstname=form.firstname.data,lastname=form.lastname.data, email=form.email.data,username=form.username.data)
        user.set_password(form.password1.data)
        student = Student(student_number=form.student_number.data,year_of_study=form.year_of_study.data,user=user)
        db.session.add(user)
        db.session.add(student)
        db.session.commit()
        flash('Congratulations, you are now a registered Student!')
        return redirect(url_for('student_home'))
    return render_template('auth/student_reg.html',title='student registation',form=form)



@app.route('/tutor/registration', methods=['GET','POST'])
def tutorRegistration():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = TutorRegForm()
    if form.validate_on_submit():
        user = User(firstname=form.firstname.data,lastname=form.lastname.data, email=form.email.data,username=form.username.data)
        user.set_password(form.password1.data)
        tutor = Tutor(id_number=form.id_number.data,user=user)
        db.session.add(user)
        db.session.add(tutor)
        db.session.commit()
        flash('Congratulations, you are now a registered Tutor!')
        return redirect(url_for('tutor_home'))
    return render_template('auth/tutor_reg.html',title='tutor registation',form=form)

@app.route('/lecture/registration', methods=['GET','POST'])
def lectureRegistration():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LectureRegForm()
    if form.validate_on_submit():
        user = User(firstname=form.firstname.data,lastname=form.lastname.data, email=form.email.data,username=form.username.data)
        user.set_password(form.password1.data)
        lecture = Lecture(employee_number=form.employee_number.data, user=user)
        db.session.add(user)
        db.session.add(lecture)
        db.session.commit()
        flash('Congratulations, you are now a registered Lecture!')
        return redirect(url_for('lecture_home'))
    return render_template('auth/lecture_reg.html',title='lecture registation',form=form)

@app.route('/student_home')
@login_required
def student_home():
    return render_template('student_home.html')

@app.route('/lecture_home')
@login_required
def lecture_home():
    return render_template('lecture_home.html')

@app.route('/tutor_home')
@login_required
def tutor_home():
    return render_template('tutor_home.html')

@app.route('/tutor/edit_profile', methods=['GET','POST'])
@login_required
def edit_tutor():
    form=EditTutorProfileForm()
    if form.validate_on_submit():
        current_user.tutor.account_type = form.account_type.data
        current_user.tutor.account_number = form.account_number.data
        current_user.tutor.bank_name = form.bank_name.data
        current_user.tutor.branch_code = form.branch_code.data
        current_user.tutor.phone_number = form.phone_number.data
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('tutor_profile'))
    elif request.method == 'GET':
        form.account_type.data = current_user.tutor.account_type
        form.account_number.data = current_user.tutor.account_number
        form.bank_name.data = current_user.tutor.bank_name
        form.branch_code.data = current_user.tutor.branch_code
        form.phone_number.data = current_user.tutor.phone_number
    return render_template('edit_tutor.html',title='edit profile', form=form)

@app.route('/lecture/edit_profile', methods=['GET','POST'])
@login_required
def edit_lecture():
    form = EditLectureProfileForm()
    if form.validate_on_submit():
        current_user.lecture.office_number = form.office_number.data
        current_user.lecture.telephone_number = form.telephone_number.data
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('lecture_profile'))
    elif request.method == 'GET':
        form.office_number.data = current_user.lecture.office_number
        form.telephone_number.data = current_user.lecture.telephone_number
    return render_template('edit_lecture.html',title='edit profile', form=form)

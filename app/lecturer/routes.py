from app import db
from flask import render_template, url_for, flash, redirect, request
from .forms import LectureRegForm,EditLectureProfileForm
from flask_login import current_user, login_required
from app.models import User, Lecture ,Tutor, Student, Course
from werkzeug.urls import url_parse
from app.lecturer import lecturer







@lecturer.route('/home')
@login_required
def lecture_home():
    return render_template('lecturer/lecture_home.html')

@lecturer.route('/profile')
@login_required
def lecture_profile():
    return render_template('lecturer/lecture_profile.html',title='profile')


@lecturer.route('/registration', methods=['GET','POST'])
def lectureRegistration():
    if current_user.is_authenticated:
        return redirect(url_for('auth.index'))
    form = LectureRegForm()
    if form.validate_on_submit():
        user = User(firstname=form.firstname.data,lastname=form.lastname.data, email=form.email.data,username=form.username.data)
        user.set_password(form.password1.data)
        lecture = Lecture(employee_number=form.employee_number.data, user=user)
        db.session.add(user)
        db.session.add(lecture)
        db.session.commit()
        flash('Congratulations, you are now a registered Lecturer!')
        return redirect(url_for('lecturer.lecture_home'))
    return render_template('lecturer/lecture_reg.html',title='lecture registation',form=form)

@lecturer.route('/edit-profile', methods=['GET','POST'])
@login_required
def edit_lecture():
    form = EditLectureProfileForm()
    if form.validate_on_submit():
        current_user.lecture.office_number = form.office_number.data
        current_user.lecture.telephone_number = form.telephone_number.data
        db.session.commit()
        flash('Your changes have been saved successfully.')
        return redirect(url_for('lecturer.lecture_profile'))
    elif request.method == 'GET':
        form.office_number.data = current_user.lecture.office_number
        form.telephone_number.data = current_user.lecture.telephone_number
    return render_template('lecturer/edit_lecture.html',title='edit profile', form=form)



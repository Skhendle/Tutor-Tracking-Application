from app import db
from flask import render_template, url_for, flash, redirect, request
from .forms import StudentRegForm
from flask_login import current_user,login_required
from app.models import User, Lecture ,Tutor, Student, Course
from werkzeug.urls import url_parse

from app.student import student




@student.route('/home')
@login_required
def student_home():
    return render_template('student/student_home.html', title = 'Student home')


@student.route('/profile')
@login_required
def student_profile():
    return render_template('student/student_profile.html',title='profile')


@student.route('/registration', methods=['GET','POST'])
def studentRegistration():
    if current_user.is_authenticated:
        return redirect(url_for('auth.index'))
    form = StudentRegForm()
    if form.validate_on_submit():# pragma: no cover
        user = User(firstname=form.firstname.data,lastname=form.lastname.data, email=form.email.data,username=form.username.data)
        user.set_password(form.password1.data)
        student = Student(student_number=form.student_number.data,year_of_study=form.year_of_study.data,user=user)
        db.session.add(user)
        db.session.add(student)
        db.session.commit()
        flash('Congratulations, you are now a registered Student!')
        return redirect(url_for('student.student_home'))
    return render_template('student/student_reg.html',title='student registation',form=form)

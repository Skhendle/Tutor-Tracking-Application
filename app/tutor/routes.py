from app import db
from flask import render_template, url_for, flash, redirect, request
from .forms import TutorRegForm , EditTutorProfileForm
from flask_login import current_user, login_required
from app.models import User, Lecture ,Tutor, Student, Course
from werkzeug.urls import url_parse

from app.tutor import tutor




@tutor.route('/home')
@login_required
def tutor_home():
    return render_template('tutor/tutor_home.html')


@tutor.route('/profile')
@login_required
def tutor_profile():
    return render_template('tutor/tutor_profile.html',title='profile')

@tutor.route('/registration', methods=['GET','POST'])
def tutorRegistration():
    if current_user.is_authenticated:
        return redirect(url_for('auth.index'))
    form = TutorRegForm()
    if form.validate_on_submit():
        user = User(firstname=form.firstname.data,lastname=form.lastname.data, email=form.email.data,username=form.username.data)
        user.set_password(form.password1.data)
        tutor = Tutor(id_number=form.id_number.data,user=user)
        db.session.add(user)
        db.session.add(tutor)
        db.session.commit()
        flash('Congratulations, you are now a registered Tutor!')
        return redirect(url_for('tutor.tutor_home'))
    return render_template('tutor/tutor_reg.html',title='tutor registation',form=form)


@tutor.route('/tutor/edit-profile', methods=['GET','POST'])
@login_required
def edit_tutor():
    form=EditTutorProfileForm()
    if form.validate_on_submit():
        current_user.tutor.account_type = form.account_type.data
        current_user.tutor.account_number = form.account_number.data
        current_user.tutor.bank_name = form.bank_name.data
        current_user.tutor.branch_code = form.branch_code.data
        current_user.tutor.phone_number = form.phone_number.data
        current_user.tutor.status = int(form.status.data)
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('tutor.tutor_profile'))
    elif request.method == 'GET':
        form.account_type.data = current_user.tutor.account_type
        form.account_number.data = current_user.tutor.account_number
        form.bank_name.data = current_user.tutor.bank_name
        form.branch_code.data = current_user.tutor.branch_code
        form.phone_number.data = current_user.tutor.phone_number
        form.status.data = current_user.tutor.status
    return render_template('tutor/edit_tutor.html',title='edit profile', form=form)


@tutor.route('/view-courses/my-courses')
@login_required
def tutor_courses():
    return render_template('tutor/tutor_courses.html', title = 'My courses')

@tutor.route('/access-a-tutor')
@login_required
def access_tutor():
    tutors = Tutor.query.all()
    return render_template('tutor/access_tutors.html', title='Access a tutors', tutors=tutors)

@tutor.route('/tutor-details/<id_number>')
@login_required
def tutor_details(id_number):
    tutor = Tutor.query.filter_by(id_number=id_number).first_or_404()
    print(tutor)
    return render_template('tutor/tutor_details.html',title='Tutor details', tutor=tutor)


    
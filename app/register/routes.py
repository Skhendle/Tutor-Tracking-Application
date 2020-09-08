from flask import render_template, flash, redirect , url_for, request
from app.register import register
from flask_login import login_required
from app.register.forms import RegisterForm 
from app.models import Register,  Course , Tutor
from app import db
import random
from flask_paginate import Pagination, get_page_parameter

@register.route('/generate-otp')
@login_required
def generate_otp():
    return render_template('register/generate_otp.html', title='generate otp')

@register.route('/capture-otp/<course_code>', methods=['POST','GET'])
@login_required
def capture_otp(course_code):
    form = RegisterForm()
    course = Course.query.filter_by(course_code=course_code).first_or_404()
    if form.validate_on_submit():
        tutor = Tutor.query.filter_by(id_number=form.id_number.data).first_or_404()
        if tutor not in course.enrolled_tutors:
            flash('Student is not enrolled in this course')
            return redirect(url_for('register.capture_otp', course_code=course_code))
        else:
            if tutor.otp == form.otp.data:
                reg =  Register(otp=form.otp.data,courses=course, attendance=tutor)    
                db.session.add(reg)
                tutor.otp = random.randint(10000000,50000000)
                db.session.commit()
                flash('The student has been capture')
                return redirect(url_for('register.capture_otp' , course_code=course_code))
            else:
                flash('The student has been capture/One time pin is invalid')
                return redirect(url_for('register.capture_otp', course_code=course_code))
    return render_template('register/capture_otp.html', title='Capture One time pin' , form = form )

@register.route('/attendance/<course_code>')
@login_required
def attendance(course_code):
    page = request.args.get('page', 1, type=int)
    attendance_list = Register.query.filter_by(course=course_code).paginate(page,2,False)
    return render_template('register/attendence_list.html',title='Attendance',attendance_list=attendance_list.items)
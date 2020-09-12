from app import db
from flask import render_template, url_for, flash, redirect, request
from app.courses.forms import CourseCreationForm , EnrollmentKeyForm, SessionRegForm, GenerateOTP
from flask_login import current_user, login_required
from app.models import User, Lecture ,Tutor, Student, Course, Session
from werkzeug.urls import url_parse
from app.courses import courses 
import random
import string

def randStr(chars = string.ascii_uppercase + string.digits, N=10):
	return ''.join(random.choice(chars) for _ in range(N))

@courses.route('/create-course' ,methods = ['GET','POST'])
@login_required
def create_course():
    form = CourseCreationForm()
    if form.validate_on_submit():
        course = Course(course_code=form.course_code.data,name=form.name.data,venue=form.venue.data,start_time=form.start_time.data,end_time=form.end_time.data,\
            day=form.day.data, number_of_tutors=form.number_of_tutors.data, lecturer=current_user.lecture)
        course.lecturer = current_user.lecture
        db.session.add(course)
        db.session.commit()
        return redirect(url_for('courses.my_courses'))
    return render_template('courses/create_course.html',title='Create a course',form=form)


# This function should allow the lecturer to create a new session for any of the courses 
# they are lecturing
@courses.route('/create_session', methods = ['GET', 'POST'])
@login_required
def create_session():
    form = SessionRegForm(current_user.lecture.course)
    if form.validate_on_submit():
        session = Session(course = form.course.data, session_start = form.start_time.data, session_end = form.end_time.data, session_date = form.date.data)
        db.session.add(session)
        db.session.commit()
        return redirect(url_for('courses.view_sessions'))
    return render_template('courses/create_session.html',title='Create a session', form=form)

A = ["Session1", "Session2"]
B = ["Session Course", "Date", "start_time", "end_time"]
# Lecturer side
# This function should display the sesions created by the current lecturer
# A nd B are mockup items to test the view
@courses.route('/view_sessions')
@login_required
def view_session():
    return render_template('courses/view_sessions.html',title='View sessions', A=A, B=B)

A = ["Session1", "Session2"]
B = ["Session Course", "Date", "start_time", "end_time", "OTP"]
# This fuunction should search if there are sessions for the current 
# tutor by checking if the are not any sessions available for the courses
# the tutor is registered for. When the tutor has an OTP already just reload page.
# 
@courses.route('/view_sessions_tutor')
@login_required
def view_sessions_tutor():
    form =  GenerateOTP()
    return render_template('courses/view_sessions_tutor.html',title='View sessions', A=A, B=B, form=form)

@courses.route('/my-courses')
@login_required
def my_courses():
    return render_template('courses/my_courses.html',title='My courses')

@courses.route('/explore')
@login_required
def explore():
    courses = Course.query.all()
    return render_template('courses/explore.html', title='explore courses', courses=courses)

@courses.route('/<course_code>')
@login_required
def show_course_details(course_code):
    course = Course.query.filter_by(course_code=course_code).first_or_404()
    return render_template('courses/show_course_details.html',title='course details', course=course)

@courses.route('/enroll/<course_code>' , methods=['GET','POST'])
@login_required
def enroll_in_a_course(course_code):
    form = EnrollmentKeyForm()
    course = Course.query.filter_by(course_code=course_code).first_or_404()
    if form.validate_on_submit():
        if current_user.student:
            current_user.student.enrolled_courses.append(course)
            db.session.commit()
            return redirect(url_for('student.student_home'))
        elif current_user.tutor:
            current_user.tutor.enrolled_courses.append(course)
            db.session.commit()
            return redirect(url_for('tutor.tutor_courses'))
    if request.method == "GET":
        form.course_code.data = course_code
    return render_template('courses/enroll.html',title=f'enroll in {course_code}' , form=form , course_code=course_code)
    


@courses.route('/course/<course_code>' , methods=['POST', 'GET'])
@login_required
def edit_course_details(course_code):
    form = CourseCreationForm()
    course = Course.query.filter_by(course_code=course_code).first_or_404()
    if form.validate_on_submit():
        course.course_code = form.course_code.data
        course.name = form.name.data
        course.venue = form.venue.data
        course.start_time = form.start_time.data
        course.end_time = form.end_time.data
        course.day = form.day.data
        course.number_of_tutors = form.number_of_tutors.data
        course.key = form.key.data
        db.session.commit()
        return redirect(url_for('courses.show_course_details', course_code=course_code))
    elif request.method == "GET":
        form.course_code.data = course.course_code 
        form.name.data = course.name
        form.venue.data = course.venue
        form.number_of_tutors.data = course.number_of_tutors 
        form.key.data = course.key
        form.start_time.data = course.start_time
        form.end_time.data = course.end_time
        form.day.data = course.day
        form.key.data = course.key
    return render_template('courses/create_course.html', title = 'Edit course details', form = form)

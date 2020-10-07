from app import db
from flask import render_template, url_for, flash, redirect, request
from app.courses.forms import CourseCreationForm , EnrollmentKeyForm
from flask_login import current_user, login_required
from app.models import User, Lecture ,Tutor, Student, Course
from werkzeug.urls import url_parse
from app.courses import courses 
import random
import string

def randStr(chars = string.ascii_uppercase + string.digits, N=10):
	# pragma: no cover
	return ''.join(random.choice(chars) for _ in range(N))

@courses.route('/create-course' ,methods = ['GET','POST'])
@login_required
def create_course():# pragma: no cover
    form = CourseCreationForm()
    if form.validate_on_submit():# pragma: no cover
        course = Course(course_code=form.course_code.data,name=form.name.data,venue=form.venue.data,start_time=form.start_time.data,end_time=form.end_time.data,\
            day=form.day.data, key=form.key.data, number_of_tutors=form.number_of_tutors.data, lecturer=current_user.lecture)
        course.lecturer = current_user.lecture
        db.session.add(course)
        db.session.commit()
        return redirect(url_for('courses.my_courses'))
    return render_template('courses/create_course.html',title='Create a course',form=form)



@courses.route('/my-courses')
@login_required
def my_courses():
    return render_template('courses/my_courses.html',title='My courses')

@courses.route('/explore')
@login_required
def explore():
    courses = Course.query.all()
    return render_template('courses/explore.html', title='explore courses', courses=courses)

@courses.route('/apply')
@login_required
def apply():# pragma: no cover
    courses = Course.query.all()
    return render_template('courses/apply.html', title='apply for a courses', courses=courses)

@courses.route('/<course_code>')
@login_required
def show_course_details(course_code):
    course = Course.query.filter_by(course_code=course_code).first_or_404()
    return render_template('courses/show_course_details.html',title='course details', course=course)

@courses.route('/enroll/<course_code>' , methods=['GET','POST'])
@login_required
def enroll_in_a_course(course_code):
    form = EnrollmentKeyForm()
    if request.method == 'GET':# pragma: no cover
        form.course_code.data = course_code
    course = Course.query.filter_by(course_code=course_code).first_or_404()
    if form.validate_on_submit():# pragma: no cover
        if current_user.student:
            current_user.student.enrolled_courses.append(course)
            db.session.commit()
            return redirect(url_for('student.student_home'))
        elif current_user.tutor:
            current_user.tutor.enrolled_courses.append(course)
            db.session.commit()
            return redirect(url_for('tutor.tutor_courses'))
    return render_template('courses/enroll.html',title=f'enroll in {course_code}' , form=form , course_code=course_code)
    


@courses.route('/course/<course_code>' , methods=['POST', 'GET'])
@login_required
def edit_course_details(course_code):
    form = CourseCreationForm()
    course = Course.query.filter_by(course_code=course_code).first_or_404()
    if form.validate_on_submit():# pragma: no cover
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
    elif request.method == "GET":# pragma: no cover
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



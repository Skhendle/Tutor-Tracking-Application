from app import app, db
from flask import render_template, url_for, flash, redirect, request
from app.forms import LoginForm, LectureRegForm, TutorRegForm , EditTutorProfileForm, EditLectureProfileForm ,StudentRegForm , CourseCreationForm
from flask_login import current_user, login_user, logout_user , login_required
from app.models import User, Lecture ,Tutor, Student, Course
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

@app.route('/student-home')
@login_required
def student_home():
    return render_template('student_home.html', title = 'Student home')

@app.route('/lecture-home')
@login_required
def lecture_home():
    return render_template('lecture_home.html')

@app.route('/tutor-home')
@login_required
def tutor_home():
    return render_template('tutor_home.html')

@app.route('/tutor/edit-profile', methods=['GET','POST'])
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
        return redirect(url_for('tutor_profile'))
    elif request.method == 'GET':
        form.account_type.data = current_user.tutor.account_type
        form.account_number.data = current_user.tutor.account_number
        form.bank_name.data = current_user.tutor.bank_name
        form.branch_code.data = current_user.tutor.branch_code
        form.phone_number.data = current_user.tutor.phone_number
        form.status.data = current_user.tutor.status
    return render_template('edit_tutor.html',title='edit profile', form=form)

@app.route('/lecture/edit-profile', methods=['GET','POST'])
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

@app.route('/courses/create-course' ,methods = ['GET','POST'])
def create_course():
    form = CourseCreationForm()
    if form.validate_on_submit():
        course = Course(course_code=form.course_code.data,name=form.name.data,venue=form.venue.data,start_time=form.start_time.data,end_time=form.end_time.data,\
            day=form.day.data, number_of_tutors=form.number_of_tutors.data,lecturer=current_user.lecture)
        db.session.add(course)
        db.session.commit()
        return redirect(url_for('my_courses'))
    return render_template('create_course.html',title='Create a course',form=form)

@app.route('/courses/my-courses')
def my_courses():
    return render_template('my_courses.html',title='My courses')

@app.route('/courses/explore')
def explore():
    courses = Course.query.all()
    return render_template('explore.html', title='explore courses', courses=courses)


@app.route('/courses/<course_code>')
def show_course_details(course_code):
    course = Course.query.filter_by(course_code=course_code).first_or_404()
    return render_template('show_course_details.html',title='course details', course=course)

@app.route('/enroll/<course_code>' , methods=['GET','POST'])
def enroll_in_a_course(course_code) :
    course = Course.query.filter_by(course_code=course_code).first_or_404()
    key = 'testing'
    if request.method == 'POST':
        entered_key = request.form['enrollment_key']
        if entered_key == key:
            if current_user.student:
                current_user.student.enrolled_courses.append(course)
                db.session.commit()
                return redirect(url_for('student_home'))
            elif current_user.tutor:
                current_user.tutor.enrolled_courses.append(course)
                db.session.commit()
                return redirect(url_for('tutor_courses'))
        else:
            return redirect(url_for('enroll_in_a_course', course_code=course_code))
    return render_template('enroll.html',title=f'enroll in {course_code}')
    
@app.route('/course/<course_code>' , methods=['POST', 'GET'])
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
        db.session.commit()
        return redirect(url_for('show_course_details', course_code=course_code))
    elif request.method == "GET":
        form.course_code.data = course.course_code 
        form.name.data = course.name
        form.venue.data = course.venue
        form.number_of_tutors.data = course.number_of_tutors 

    return render_template('create_course.html', title = 'Edit course details', form = form)

    
@app.route('/tutor/view-courses/my-courses')
def tutor_courses():
    return render_template('tutor_courses.html', title = 'My courses')

@app.route('/tutors/access-a-tutor')
def access_tutor():
    tutors = Tutor.query.all()
    return render_template('access_tutors.html', title='Access a tutors', tutors=tutors)

@app.route('/tutors/tutor-details/<id_number>')
def tutor_details(id_number):
    tutor = Tutor.query.filter_by(id_number=id_number).first_or_404()
    print(tutor)
    return render_template('tutor_details.html',title='Tutor details', tutor=tutor)


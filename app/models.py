from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login
import random
import json
from time import time


#User mixin extends the user model to add three fields required to manage a user
#is_authenticated, is_active ,is-anonymous and get_id() method
@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    firstname = db.Column(db.String(60), nullable=False)
    lastname = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(255),nullable=False, unique=True)
    username = db.Column(db.String(120),nullable=False, index=True, unique=True)
    password_hash = db.Column(db.String(120),nullable=False, unique=True)
    create_date = db.Column(db.DateTime , index=True,default=datetime.now)
    lecture = db.relationship('Lecture', backref='user', uselist=False, lazy=True)
    tutor = db.relationship('Tutor', backref='user', uselist=False, lazy=True)
    student = db.relationship('Student', backref='user', uselist=False, lazy=True)
    messages_sent = db.relationship('Message',
                                    foreign_keys='Message.sender_id',
                                    backref='author', lazy='dynamic')
    messages_received = db.relationship('Message',
                                        foreign_keys='Message.recipient_id',
                                        backref='recipient', lazy='dynamic')
    last_message_read_time = db.Column(db.DateTime)

    notifications = db.relationship('Notification', backref='user',
                                    lazy='dynamic')


    def add_notification(self, name, data):
        self.notifications.filter_by(name=name).delete()
        n = Notification(name=name, payload_json=json.dumps(data), user=self)
        db.session.add(n)
        return n


    def new_messages(self):
        last_read_time = self.last_message_read_time or datetime(1900, 1, 1)
        return Message.query.filter_by(recipient=self).filter(
            Message.timestamp > last_read_time).count()

    def __repr__(self):
        return 'User {}'.format(self.username)

    def set_password(self,password):
        self.password_hash = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password_hash,password)
    


"""
Because Flask-Login knows nothing about databases,it needs the application's help in loading a user
For that reason, the extension expects that the application will configure a user loader function
that can be called to load a user given the ID.
"""




class Lecture(db.Model):
    employee_number = db.Column(db.String(10),primary_key=True)
    office_number = db.Column(db.String(10),unique=True)
    telephone_number = db.Column(db.String(12),unique=True)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)
    course = db.relationship('Course', backref='lecturer',lazy=True)
    
    def __repr__(self):
        return 'Lecture {}'.format(self.employee_number)



class Tutor(db.Model):
    id_number = db.Column(db.String(10), primary_key=True)
    account_type = db.Column(db.String(60))
    account_number = db.Column(db.String(60))
    bank_name = db.Column(db.String(60))
    branch_code = db.Column(db.String(20))
    phone_number = db.Column(db.String(10))
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)
    courses = db.relationship('Course', secondary='tutors_and_courses' , backref='enrolled_tutors' , lazy=True)
    status = db.Column(db.Boolean, default=True)
    application = db.relationship('Application',backref='tutors',lazy=True)
    register = db.relationship('Register',backref='attendance',lazy=True)
    otp = db.Column(db.String(20),default=random.randint(10000000,50000000))
    
    def get_all_application_courses(self):
        applications = self.application
        application_list = [application.courses for application in applications ]
        return application_list

    def __repr__(self):
        return f'Tutor {self.id_number}'



class Student(db.Model):
    student_number = db.Column(db.String(10), primary_key=True)
    year_of_study = db.Column(db.String(2), nullable=False)
    phone_number = db.Column(db.String(10))
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)
    courses = db.relationship('Course', secondary='students_and_courses' , backref='enrolled_students' , lazy=True)

    def __repr__(self):
        return f'Student {self.student_number}'


class Course(db.Model):
    course_code = db.Column(db.String(50), primary_key=True)
    name = db.Column(db.String(120), nullable = False)
    venue = db.Column(db.String(120), nullable = False)
    start_time = db.Column(db.Time, nullable = False)
    end_time = db.Column(db.Time, nullable = False)
    day = db.Column(db.Date,nullable = False)
    number_of_tutors = db.Column(db.Integer, nullable = False)
    Lecture_employee_number = db.Column(db.String(20), db.ForeignKey('lecture.employee_number'), nullable = False)
    students = db.relationship('Student', secondary='students_and_courses', backref='enrolled_courses', lazy=True)
    tutors = db.relationship('Tutor', secondary='tutors_and_courses', backref='enrolled_courses', lazy=True)
    key = db.Column(db.String(120))
    application = db.relationship('Application',backref='courses',lazy=True)
    register = db.relationship('Register',backref='courses',lazy=True)
    forum = db.relationship('Forum',backref='forum_course', uselist=False ,lazy=True)

    def __repr__(self):
        return f'Course {self.course_code}'

#Association table students
students_and_courses = db.Table('students_and_courses',
    db.Column('student_number',db.String(20), db.ForeignKey('student.student_number'), primary_key = True),
    db.Column('course_code',db.String(20),db.ForeignKey('course.course_code'),primary_key=True)
)


#Association Table tutors
tutors_and_courses = db.Table('tutors_and_courses',
    db.Column('id_number',db.String(20), db.ForeignKey('tutor.id_number'), primary_key=True),
    db.Column('course_code',db.String(20),db.ForeignKey('course.course_code'),primary_key=True)
)


class Application(db.Model):
    applicaton_id = db.Column(db.Integer, primary_key=True)
    motivation = db.Column(db.String(2048), nullable=False)
    academic_record = db.Column(db.String(255))
    course = db.Column(db.String(50), db.ForeignKey('course.course_code'))
    tutor = db.Column(db.String(15), db.ForeignKey('tutor.id_number'))
    status = db.Column(db.String(10))

    def __repr__(self):
        return f'Application {self.course} by {self.tutor}'


class Register(db.Model):
    register_id = db.Column(db.Integer, primary_key=True)
    otp = db.Column(db.String(50), nullable = False)
    session = db.Column(db.DateTime ,default=datetime.now)
    course = db.Column(db.String(50), db.ForeignKey('course.course_code'))
    tutor = db.Column(db.String(15), db.ForeignKey('tutor.id_number')) 

    def __repr__(self):
        return f'Register {self.register_id}'
    
class Message(db.Model):
    message_id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    recipient_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    forum_recipt_id = db.Column(db.Integer, db.ForeignKey('forum.forum_id'))
    body = db.Column(db.String(30000))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.now)


    def __repr__(self):
        return f'Message {self.message_id}'

class Notification(db.Model):
    notification_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    timestamp = db.Column(db.Float, index=True, default=time)
    payload_json = db.Column(db.Text)

    def get_data(self):
        return json.loads(str(self.payload_json))

class Forum(db.Model):
    forum_id = db.Column(db.Integer, primary_key=True)
    course = db.Column(db.String(50), db.ForeignKey('course.course_code'))
    messages_received = db.relationship('Message',
                                        foreign_keys='Message.forum_recipt_id',
                                        backref='forum', lazy='dynamic')


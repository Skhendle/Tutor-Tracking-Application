from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login


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
    create_date = db.Column(db.DateTime , index=True,default=datetime.utcnow)
    lecture = db.relationship('Lecture', backref='user', uselist=False, lazy=True)
    tutor = db.relationship('Tutor', backref='user', uselist=False, lazy=True)
    student = db.relationship('Student', backref='user', uselist=False, lazy=True)


    def __repr__(self):
        return f'User {self.username}'

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
        return f'Lecture {self.employee_number}'



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
    start_time = db.Column(db.String(120), nullable = False)
    end_time = db.Column(db.String(120), nullable = False)
    day = db.Column(db.String(120),nullable = False)
    number_of_tutors = db.Column(db.Integer, nullable = False)
    Lecture_employee_number = db.Column(db.String(20), db.ForeignKey('lecture.employee_number'), nullable = False)
    students = db.relationship('Student', secondary='students_and_courses', backref='enrolled_courses', lazy=True)
    tutors = db.relationship('Tutor', secondary='tutors_and_courses', backref='enrolled_courses', lazy=True)

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

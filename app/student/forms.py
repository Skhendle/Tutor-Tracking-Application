from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, ValidationError , SelectField , RadioField
from wtforms.validators import DataRequired, Email, EqualTo , Length
from app.models import Student, User

from app.auth.forms import validate_employee_student_number

class StudentRegForm(FlaskForm):
    firstname = StringField('Your Name', validators=[DataRequired()])
    lastname = StringField('Your Surname', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    student_number = StringField('Student Number',validators=[DataRequired(), validate_employee_student_number])
    year_of_study = SelectField('Year of study', choices=[('1','1'),('2', '2'), ('3', '3'), ('4', '4'),('4+','4+')])
    password1 = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password1',message='Passwords must match')])
    submit = SubmitField('Create account')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')
    
    def validate_student_number(self, student_number):
        number = Student.query.filter_by(student_number=student_number.data).first()
        if number is not None:
            raise ValidationError('Your student number is already registered.')
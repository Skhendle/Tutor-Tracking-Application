from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, ValidationError , SelectField , RadioField
from wtforms.validators import DataRequired, Email, EqualTo , Length
from app.models import Lecture,User

from app.auth.forms import validate_employee_student_number , validate_phone_number


class LectureRegForm(FlaskForm):
    firstname = StringField('Your Name', validators=[DataRequired()])
    lastname = StringField('Your Surname', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    employee_number = StringField('Employee Number',validators=[DataRequired(), validate_employee_student_number])
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

    def validate_employee_number(self, employee_number):
        number = Lecture.query.filter_by(employee_number=employee_number.data).first()
        if number is not None:
            raise ValidationError('Your employee number is already registered.')


class EditLectureProfileForm(FlaskForm):
    office_number = StringField('Office number',validators=[validate_employee_student_number])
    telephone_number = StringField('Telephone number',validators=[validate_phone_number])
    submit = SubmitField('Update')
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, ValidationError , SelectField
from wtforms.validators import DataRequired, Email, EqualTo
from app.models import User
import re


def validate_employee_student_number(form, field):
    if len(field.data) > 10:
        raise ValidationError('number must be less than 10 characters')
    myReg = re.search(r'^\d+$',field.data)
    if myReg == None:
        raise ValidationError('number is invalid')
    return None
        

def validate_phone_number(form, field):
    if len(field.data) != 10:
        raise ValidationError('phone number is invalid')
    myReg = re.search(r'^\d+$',field.data)
    if myReg == None:
        raise ValidationError('phone number is invalid')
    return None


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

    
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
    


class TutorRegForm(FlaskForm):
    firstname = StringField('Your Name', validators=[DataRequired()])
    lastname = StringField('Your Surname', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    student_number = StringField('Student Number',validators=[DataRequired(), validate_employee_student_number])
    year_of_study = SelectField('Year of study', choices=[('2', '2'), ('3', '3'), ('4', '4'),('4+','4+')])
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

            
class EditTutorProfileForm(FlaskForm):
    account_type = SelectField('Year of study', choices=[('Tr', 'Transactional'), ('Db', 'Debit'), ('Sv', 'Savings')])
    account_number = StringField('Account number')
    bank_name = StringField('Bank name')
    branch_code = StringField('Branch code')
    phone_number = StringField('My phone number',validators=[validate_phone_number])
    submit = SubmitField('Update')

    
class EditLectureProfileForm(FlaskForm):
    office_number = StringField('Office number',validators=[validate_employee_student_number])
    telephone_number = StringField('Telephone number',validators=[validate_phone_number])
    submit = SubmitField('Update')

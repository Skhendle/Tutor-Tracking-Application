from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
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


    
    


















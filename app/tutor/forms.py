from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, ValidationError , SelectField , RadioField
from wtforms.validators import DataRequired, Email, EqualTo
from app.models import Tutor , User
from app.auth.forms import validate_employee_student_number

class TutorRegForm(FlaskForm):
    firstname = StringField('Your Name', validators=[DataRequired()])
    lastname = StringField('Your Surname', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    id_number = StringField('Identity Number',validators=[DataRequired(), validate_employee_student_number])
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

    def validate_id_number(self, id_number):
        number = Tutor.query.filter_by(id_number=id_number.data).first()
        if number is not None:
            raise ValidationError('Your id number is already registered.')


class EditTutorProfileForm(FlaskForm):
    account_type = SelectField('Year of study', choices=[('Tr', 'Transactional'), ('Db', 'Debit'), ('Sv', 'Savings')])
    account_number = StringField('Account number')
    bank_name = StringField('Bank name')
    branch_code = StringField('Branch code')
    phone_number = StringField('My phone number')
    status = RadioField('Status', choices=[('1','Available'),('0','Busy')])
    submit = SubmitField('Update')
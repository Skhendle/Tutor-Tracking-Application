from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired
from app.models import Tutor

class RegisterForm(FlaskForm):
    id_number = StringField('Your id number' , validators=[DataRequired()])
    otp = StringField('One time pin' , validators=[DataRequired()])
    submit = SubmitField('Capture')

    def validate_id_number(self,id_number):
         tutor =  Tutor.query.filter_by(id_number=id_number.data).first()
         if tutor is None:
             raise ValidationError('This tutor does not exit')
             

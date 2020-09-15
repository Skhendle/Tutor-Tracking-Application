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

    def validate_otp(self,id_number):
         tutor =  Tutor.query.filter_by(id_number=self.id_number.data).first()
         if tutor is not None:
            if self.otp.data != tutor.otp:
                raise ValidationError('Tutor OTP has been captured for this session/Tutor OTP is invalid')
             

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class RegisterForm(FlaskForm):
    id_number = StringField('Your id number' , validators=[DataRequired()])
    otp = StringField('One time pin' , validators=[DataRequired()])
    submit = SubmitField('Capture')
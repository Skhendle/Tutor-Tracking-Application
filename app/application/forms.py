from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired , FileAllowed
from werkzeug.utils import secure_filename
from wtforms import TextAreaField, PasswordField, BooleanField, SubmitField, ValidationError , SelectField , RadioField
from wtforms.validators import DataRequired , Length
from wtforms.fields.html5 import DateField, TimeField ,IntegerField
from app.models import Application
import re

class ApplicationForm(FlaskForm):
    motivation = TextAreaField('Motivation', validators=[DataRequired(), Length(min=0, max=500)])
    academic_record = FileField('Your academic record', validators=[FileRequired()])
    submit = SubmitField('Apply')

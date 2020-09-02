from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired , FileAllowed
from werkzeug.utils import secure_filename
from wtforms import StringField, PasswordField, BooleanField, SubmitField, ValidationError , SelectField , RadioField
from wtforms.validators import DataRequired
from wtforms.fields.html5 import DateField, TimeField ,IntegerField
from app.models import Application
import re

class ApplicationForm(FlaskForm):
    motivation = StringField('Motivation', validators=[DataRequired()])
    academic_record = FileField('Your academic record', validators=[FileRequired()])
    submit = SubmitField('Apply')

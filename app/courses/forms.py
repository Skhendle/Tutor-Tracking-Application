from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, ValidationError , SelectField , RadioField
from wtforms.validators import DataRequired
from wtforms.fields.html5 import DateField, TimeField ,IntegerField
import re


class CourseCreationForm(FlaskForm):
    course_code = StringField('Course code',validators=[DataRequired()]) 
    name = StringField('Course name',validators=[DataRequired()])
    venue = StringField('Venue',validators=[DataRequired()])
    start_time = TimeField('Start at')
    end_time = TimeField('End at')
    day = DateField('Day')
    number_of_tutors = IntegerField('Number of tutors',default=0, validators=[DataRequired()])
    submit = SubmitField('Create/Update course')
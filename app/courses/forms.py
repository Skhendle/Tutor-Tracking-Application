from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, ValidationError , SelectField , RadioField
from wtforms.validators import DataRequired
from wtforms.fields.html5 import DateField, TimeField ,IntegerField
from app.models import Course

class GenerateOTP(FlaskForm):
    submit = SubmitField('Generate OTP')

class SessionRegForm(FlaskForm):
    course = StringField('Course code',validators=[DataRequired()])
    start_time = TimeField('Start at', validators=[DataRequired()])
    end_time = TimeField('End at', validators=[DataRequired()])
    date = DateField('Day', validators=[DataRequired()])
    submit = SubmitField('Create sesion')


class CourseCreationForm(FlaskForm):
    course_code = StringField('Course code',validators=[DataRequired()]) 
    name = StringField('Course name',validators=[DataRequired()])
    venue = StringField('Venue',validators=[DataRequired()])
    start_time = TimeField('Start at')
    end_time = TimeField('End at')
    day = DateField('Day')
    number_of_tutors = IntegerField('Number of tutors',default=0, validators=[DataRequired()])
    submit = SubmitField('Create/Update course')
    key = StringField('Enrollment key',validators=[DataRequired()])

    def validate_course_code(self,course_code):
         course =  Course.query.filter_by(course_code=course_code.data).first()
         if course is not None:
             raise ValidationError('A Course with the name already exits')     

class EnrollmentKeyForm(FlaskForm):
    key = StringField('Enrollment key',validators=[DataRequired()])
    course_code = StringField('course code',validators=[DataRequired()])
    submit = SubmitField('Enroll')


    def validate_key(self,course_code):
        course =  Course.query.filter_by(course_code=self.course_code.data).first()
        if self.key.data != course.key:
            raise ValidationError('Incorrect key entered')

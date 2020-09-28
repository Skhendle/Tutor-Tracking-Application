from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired , FileAllowed
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class MessageForm(FlaskForm):
    message = StringField('Message', validators=[DataRequired(), Length(min=1, max=30000)])
    message_attachment = FileField('Your attachment')
    submit = SubmitField('Send')

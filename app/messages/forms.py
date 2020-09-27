from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class MessageForm(FlaskForm):
    message = StringField('Message', validators=[DataRequired(), Length(min=1, max=30000)])
    submit = SubmitField('Send')

from app import db
from config import basedir
from flask import render_template, url_for, flash, redirect, request , send_from_directory
from app.application.forms import ApplicationForm
from flask_login import current_user, login_required
from app.models import Application,Course, Message
from werkzeug.utils import secure_filename
from app.messages import messages
import os


@messages.route('/notifications')
@login_required
def notifications():
    if current_user.lecture:
        messages = current_user.lecture.messages
        for message in messages:
            if message.status == 0:
                message.status = 1      
    elif current_user.tutor:
        messages = current_user.tutor.messages
        for message in messages:
            if message.status == 0:
                message.status = 1 
    db.session.commit()
    return render_template('messages/notifications.html' , title='Notification', messages=messages)
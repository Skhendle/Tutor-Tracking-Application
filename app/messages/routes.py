from app import db
from config import basedir
from flask import render_template, url_for, flash, redirect, request , send_from_directory, current_app
from app.messages.forms import MessageForm
from flask_login import current_user, login_required
from app.models import Application,Course, Message, User
from werkzeug.utils import secure_filename
from app.messages import messages
import os
from datetime import datetime


@messages.route('/send_message/<recipient>', methods=['GET', 'POST'])
@login_required
def send_message(recipient):
    user = User.query.filter_by(username=recipient).first_or_404()
    form = MessageForm()
    if form.validate_on_submit():
        msg = Message(author=current_user, recipient=user,body=form.message.data)
        user.add_notification('unread_message_count', user.new_messages())
        db.session.add(msg)
        db.session.commit()
        flash('Your message has been sent.')
        return redirect(url_for('messages.send_message' ,recipient=user.username))
    return render_template('messages/send_message.html', title='Send Message',
                           form=form, recipient=recipient)



@messages.route('/notifications')
@login_required
def notifications():
    since = request.args.get('since', 0.0, type=float)
    notifications = current_user.notifications.filter(
        Notification.timestamp > since).order_by(Notification.timestamp.asc())
    return jsonify([{
        'name': n.name,
        'data': n.get_data(),
        'timestamp': n.timestamp} for n in notifications])

@messages.route('/')
@login_required
def messages():
    current_user.last_message_read_time = datetime.utcnow()
    current_user.add_notification('unread_message_count', 0)
    db.session.commit()
    page = request.args.get('page', 1, type=int)
    messages = current_user.messages_received.order_by(
        Message.timestamp.desc()).paginate(
            page, current_app.config['POSTS_PER_PAGE'], False)
    next_url = url_for('messages.messages', page=messages.next_num) \
        if messages.has_next else None
    prev_url = url_for('messages.messages', page=messages.prev_num) \
        if messages.has_prev else None
    return render_template('messages/messages.html', messages=messages.items,
                           next_url=next_url, prev_url=prev_url)



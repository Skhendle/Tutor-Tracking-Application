from app import db
from config import basedir
from flask import render_template, url_for, flash, redirect, request , send_from_directory, current_app , jsonify
from app.messages.forms import MessageForm
from flask_login import current_user, login_required
from app.models import Application,Course, Message, User , Course ,Forum, Notification
from werkzeug.utils import secure_filename
from app.messages import messages
import os
from datetime import datetime

UPLOAD_FOLDER = os.path.join(basedir,'app\static\message_attachments')

@messages.route('/send_message/<recipient>', methods=['GET', 'POST'])
@login_required
def send_message(recipient):
    user = User.query.filter_by(username=recipient).first_or_404()# pragma: no cover
    form = MessageForm()# pragma: no cover
    if form.validate_on_submit():# pragma: no cover
        msg = Message(author=current_user, recipient=user,
                      body=form.message.data)
        db.session.add(msg)
        db.session.commit()
        flash('Your message has been sent.')
        return redirect(url_for('tutor.tutor_details', id_number=user.tutor.id_number))
    return render_template('messages/send_message.html', title='Send Message',
                           form=form, recipient=recipient)# pragma: no cover

@messages.route('/notifications')
@login_required
def notifications():
    since = request.args.get('since', 0.0, type=float)# pragma: no cover
    notifications = current_user.notifications.filter(
        Notification.timestamp > since).order_by(Notification.timestamp)# pragma: no cover
    return jsonify([{
        'name': n.name,
        'data': n.get_data(),
        'timestamp': n.timestamp
    } for n in notifications])# pragma: no cover


@messages.route('/add-forum/<course_code>')
@login_required
def add_forum(course_code):
    course = Course.query.filter_by(course_code = course_code).first_or_404()# pragma: no cover
    if course.forum:# pragma: no cover
        flash("forum already exits for this course")
        redirect(url_for('courses.show_course_details' , course_code=course_code))
    else:# pragma: no cover
        forum = Forum(forum_course=course)
        db.session.add(forum)
        db.session.commit()
        flash("forum has been successfully created for you course")
        redirect(url_for('courses.show_course_details' , course_code=course_code))
    return redirect(url_for('courses.show_course_details' , course_code=course_code))# pragma: no cover

@messages.route('/unread_messages/<course>' , methods=['GET'])
@login_required
def unread_messages(course):
    forum = Forum.query.filter_by(course=course).first_or_404()# pragma: no cover
    last_message = forum.messages_received.all()[-1]# pragma: no cover
    if last_message.timestamp > current_user.last_message_read_time:# pragma: no cover
        return "True"
    else:# pragma: no cover
        return "False"


@messages.route('/<course_code>/forum' , methods=['GET','POST'])
@login_required
def forum_messages(course_code):
    current_user.last_message_read_time = datetime.now()# pragma: no cover
    db.session.commit()# pragma: no cover
    form = MessageForm()# pragma: no cover
    forum = Forum.query.filter_by(course=course_code).first_or_404()# pragma: no cover
    course = Course.query.filter_by(course_code = course_code).first_or_404()# pragma: no cover
    ordered_messages = forum.messages_received.order_by(Message.upvote_count.desc())# pragma: no cover
    if request.method ==  'GET':# pragma: no cover
        page = request.args.get('page', 1, type=int)
        messages = forum.messages_received.paginate(
                page, current_app.config['POSTS_PER_PAGE'], False)
        next_url = url_for('messages.forum_messages',course_code=course_code ,page=messages.next_num) \
            if messages.has_next else None
        prev_url = url_for('messages.forum_messages',course_code=course_code, page=messages.prev_num) \
            if messages.has_prev else None
     
    if form.validate_on_submit():# pragma: no cover
        myfile = request.files['message_attachment']
        if form.message.data == '':
            if myfile.filename =='':
                return redirect(url_for('messages.forum_messages' ,course_code=course_code))
        if myfile.filename  == '':
            msg = Message(author=current_user,body=form.message.data , forum=forum, upvote_count = 0)
        else:# pragma: no cover
            filename = secure_filename(myfile.filename)
            myfile.save(os.path.join(UPLOAD_FOLDER,filename))
            msg = Message(author=current_user,body=form.message.data , forum=forum ,attachment_name=filename , upvote_count=0)
            
        db.session.add(msg)
        db.session.commit()
        
        return redirect(url_for('messages.forum_messages' ,course_code=course_code))
    return render_template('messages/forum_messages.html', title='forum messages', messages=messages.items,
                           next_url=next_url, prev_url=prev_url , form=form, course_code=course_code, ordered_messages=ordered_messages)# pragma: no cover


@messages.route('/upvote/<int:message_id>/<course_code>')
@login_required
def upvote_count(message_id, course_code):
    message = Message.query.get(message_id)# pragma: no cover
    if message.upvote_count == None:# pragma: no cover
        message.upvote_count=1
    else:# pragma: no cover
        message.upvote_count+=1
    db.session.add(message)# pragma: no cover
    db.session.commit()# pragma: no cover
    return redirect(url_for('messages.forum_messages' , course_code=course_code))# pragma: no cover



@messages.route('/<filename>')
@login_required
def message_attachment(filename):
    return send_from_directory(UPLOAD_FOLDER,filename)# pragma: no cover


@messages.route('/<course_code>/highest-upvote')
@login_required
def highest_upvote(course_code):
    forum = Forum.query.filter_by(course=course_code).first_or_404()# pragma: no cover
    course = Course.query.filter_by(course_code = course_code).first_or_404()# pragma: no cover
    if request.method ==  'GET':# pragma: no cover
        messages = forum.messages_received.order_by(Message.upvote_count.desc())
    return render_template('messages/highest_upvote.html', title='Highest upvote', messages=messages)# pragma: no cover


@messages.route('/')
@login_required
def messages():
    current_user.last_message_read_time = datetime.now()# pragma: no cover
    current_user.add_notification('unread_message_count', 0)# pragma: no cover
    db.session.add(current_user)# pragma: no cover
    db.session.commit()# pragma: no cover
    page = request.args.get('page', 1, type=int)# pragma: no cover
    messages = current_user.messages_received.order_by(
        Message.timestamp.desc()).paginate(
            page, current_app.config['POSTS_PER_PAGE'], False)# pragma: no cover
    next_url = url_for('messages.messages', page=messages.next_num) \
        if messages.has_next else None# pragma: no cover
    prev_url = url_for('messages.messages', page=messages.prev_num) \
        if messages.has_prev else None# pragma: no cover
    return render_template('messages/messages.html', title='messages', messages=messages.items,
                           next_url=next_url, prev_url=prev_url)# pragma: no cover



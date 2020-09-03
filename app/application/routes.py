from app import db
from config import basedir
from flask import render_template, url_for, flash, redirect, request
from app.application.forms import ApplicationForm
from flask_login import current_user, login_required
from app.models import Application,Course
from werkzeug.utils import secure_filename
from app.application import application
import os

UPLOAD_FOLDER = os.path.join(basedir,'app\static\\academic_records')

@application.route('/applicaton-form/<course_code>' , methods=['POST','GET'])
@login_required
def application_form(course_code):
    form = ApplicationForm()
    course = Course.query.filter_by(course_code=course_code).first_or_404()
    if form.validate_on_submit():
        file = form.academic_record.data
        filename = secure_filename(file.filename)
        file.save(os.path.join(UPLOAD_FOLDER,filename))
        application = Application(motivation=form.motivation.data,academic_record=filename,status='Pending',courses=course , tutors=current_user.tutor)
        db.session.add(application)
        db.session.commit()
        return redirect(url_for('courses.apply'))
    return render_template('application/application_form.html', title='Application form' , form=form , course_code=course_code)

@application.route('/my-applications')
@login_required
def my_applications():
    return render_template('application/my_applications.html', title='My applications')


from app import app, db
from app.models import User, Lecture, Tutor , Student , Course , students_and_courses

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Lecture': Lecture, 'Tutor':Tutor , 'Student':Student, 'Course':Course, 'students_and_courses':students_and_courses}


def start_ngrok():
    from pyngrok import ngrok


    url = ngrok.connect(5000)
    print('Tunnel URL:',url)

#start_ngrok()

'''
if app.config['START_NGROK']:
    start_ngrok():
'''
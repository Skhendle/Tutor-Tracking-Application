from app import create_app ,db
from app.models import User, Lecture ,Tutor , tutors_and_courses , Student ,students_and_courses

app = create_app()


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Lecture':Lecture , 'Tutor':Tutor , 'tutors_and_courses':tutors_and_courses,'Student':Student,'students_and_courses':students_and_courses }

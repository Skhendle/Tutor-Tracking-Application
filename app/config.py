import os


#using a class to store configuration variables
class Config(object):
    START_NGROK = os.environ.get('START_NGROK') is not None
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = 'mysql://root:It740039@localhost/tutortracker'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')
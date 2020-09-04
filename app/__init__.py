from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import os
from config import basedir


db = SQLAlchemy()
migrate = Migrate()
login = LoginManager() 
login.login_view = 'auth.login'

def create_app(config_class=Config):
    UPLOAD_FOLDER = os.path.join(basedir,'static\academic_records') 

    app = Flask(__name__)
    app.config.from_object(config_class)


    db.init_app(app)
    migrate.init_app(app,db)
    login.init_app(app)



    from app.auth import auth
    from app.lecturer import lecturer 
    from app.tutor import tutor
    from app.student import student
    from app.courses import courses
    from app.application import application
    from app.messages import messages



    app.register_blueprint(auth)
    app.register_blueprint(lecturer)
    app.register_blueprint(tutor)
    app.register_blueprint(student)
    app.register_blueprint(courses)
    app.register_blueprint(application)
    app.register_blueprint(messages)

    return app

from app import models


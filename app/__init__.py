from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


db = SQLAlchemy()
migrate = Migrate()
login = LoginManager() 
login.login_view = 'auth.login'

def create_app(config_class=Config):

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



    app.register_blueprint(auth)
    app.register_blueprint(lecturer)
    app.register_blueprint(tutor)
    app.register_blueprint(student)
    app.register_blueprint(courses)

    return app

from app import models


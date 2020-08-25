from flask import Flask
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager



app = Flask(__name__)
app.config.from_object(Config)

#flask_login instanciation
login = LoginManager(app) 
login.login_view = 'login'

#flask-sqlalchemy database instanciation
db = SQLAlchemy(app)

#flask-migrate instanciation
Migrate(app,db)


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



from app import models


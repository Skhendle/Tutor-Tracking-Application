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

from app import routes , models
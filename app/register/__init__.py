from flask import Blueprint

register = Blueprint('register',__name__,url_prefix='/register')

from app.register import routes
from flask import Blueprint

courses = Blueprint('courses',__name__,url_prefix='/courses')

from app.courses import routes
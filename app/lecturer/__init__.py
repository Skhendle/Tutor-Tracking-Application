from flask import Blueprint

lecturer = Blueprint('lecturer', __name__,url_prefix='/lecturer')

from app.lecturer import routes
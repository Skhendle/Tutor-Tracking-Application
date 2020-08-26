from flask import Blueprint

tutor = Blueprint('tutor', __name__,url_prefix='/tutor')

from app.tutor import routes
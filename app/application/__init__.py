from flask import Blueprint

application = Blueprint('application', __name__,url_prefix='/application')

from app.application import routes
from flask import Blueprint

messages = Blueprint('messages', __name__, url_prefix='/messages')

from app.messages import routes
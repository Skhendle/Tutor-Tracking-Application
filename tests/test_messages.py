import pytest
from flask import url_for

"""Testing if messaging routes are working"
test_messages_home:
test_notification_home:
test_sending_messages:
"""

"Test if messages home route is working"
def test_messages_home(flask_app_client):
    client = flask_app_client
    request = client.get('/messages/',follow_redirects=True)
    assert request.status_code == 200 

"Test if the notification route is working"
def test_notification_home(flask_app_client):
    client = flask_app_client
    request = client.get('/messages/notifications',follow_redirects=True)
    assert request.status_code == 200 

"Test if message sending route is working"
def test_sending_messages(flask_app_client):
    client = flask_app_client
    request = client.get('/messages/send_message/<recepient>',follow_redirects=True)
    assert request.status_code == 200 

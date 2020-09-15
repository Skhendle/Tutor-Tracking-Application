import pytest
from flask import url_for

def test_welcome_page(flask_app_client):
    response = flask_app_client.get('/welcome-page')
    assert b'Welcome to TUTOR TRACKER' in response.data

def test_password(flask_app_client):
    client = flask_app_client
    request = client.post('/login' , data=dict(
        username='sj_majola',password='18032009'),follow_redirects=True)
    assert request.status_code == 200

def test_counter_login_password(flask_app_client):
    client = flask_app_client
    request = client.post('/login' , data=dict(
        username='sj_majola',password=''),follow_redirects=True)
    assert request.status_code == 200

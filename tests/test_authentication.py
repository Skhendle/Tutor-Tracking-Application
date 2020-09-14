import pytest
from flask import url_for


def test_index(flask_app_client):
    client = flask_app_client
    request = client.get('/')
    assert request.status_code == 200


def test_login(flask_app_client):
    client = flask_app_client
    request = client.post('/login' , data=dict(
        username='tutor1demo',password='1234'),follow_redirects=True)
    assert request.status_code == 200

def test_tutor_registration(flask_app_client):
    client = flask_app_client
    request = client.post('/tutor/registration', data=dict(
        firtname='test',
        lastname='dummy',
        username='testdummy',
        email='testdummy@example.com',
        id_number='000000002',
        password1='1234',
        password2='1234'),follow_redirects=True)
    assert request.status_code == 200


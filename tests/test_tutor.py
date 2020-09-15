import pytest
from flask import url_for


"""
Testing the tutor functionality.

test_index: Tests if a tutor  can access the website basic page

test_login_pass, def test_tutor_logout: Testing whether a tutor can 
successfully login and logout since we re-direct loggin page for login out

test_welcome_page: Testing the data in the welcome page after loggin

test_tutor_registration: Tesing if a tutor can register to the website

test_tutor_dashboard: Testing whether the tutor can access can access
the dashboard after login.

test_tutor_profile: Testing whether a tutor can access the profile settings page.

test_tutor_application: Testing whether a tutor can access the application page.

"""
def test_index(flask_app_client):
    client = flask_app_client
    request = client.get('/')
    assert request.status_code == 200


def test_login_pass(flask_app_client):
    client = flask_app_client
    request = client.post('/login' , data=dict(
        username='tutor1demo',password='1234'),follow_redirects=True)
    assert request.status_code == 200

def test_login_fail(flask_app_client):
    client = flask_app_client
    request = client.post('/login' , data=dict(
        username='tutor1demo',password=''),follow_redirects=True)
    assert request.status_code == 200

def test_welcome_page(flask_app_client):
    response = flask_app_client.get('/welcome-page')
    assert b'Welcome to TUTOR TRACKER' in response.data

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

def test_tutor_dashboard(flask_app_client):
    client = flask_app_client
    request = client.get('/tutor/home',follow_redirects=True)
    assert request.status_code == 200

def test_tutor_profile(flask_app_client):
    client = flask_app_client
    request = client.get('/tutor/profile',follow_redirects=True)
    assert request.status_code == 200

def test_tutor_application(flask_app_client):
    client = flask_app_client
    request = client.get('/application/my-applications',follow_redirects=True)
    assert request.status_code == 200

def test_tutor_get_otp(flask_app_client):
    client = flask_app_client
    request = client.get('/register/generate-otp',follow_redirects=True)
    assert request.status_code == 200

def test_tutor_logout(flask_app_client):
    client = flask_app_client
    request = client.get('/register/generate-otp',follow_redirects=True)
    assert request.status_code == 200

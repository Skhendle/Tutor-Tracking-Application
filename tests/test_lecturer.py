import pytest
from flask import url_for

"""
Testing the lecturer functionality.
test_index: Tests if a lecturer  can access the website basic page
test_login_pass, test_tutor_logout: Testing whether a tutor can 
successfully login and logout since we re-direct loggin page for login out
test_welcome_page: Testing the data in the welcome page after loggin
test_lecturer_registration: Tesing if a tutor can register to the website
test_tutor_dashboard: Testing whether the tutor can access can access
the dashboard after login.
test_lecturer_profile: Testing whether a tutor can access the profile settings page.
test_lecturer_profile_edit: Testing whether the lecturer can edit the profile
"""

"Test the welcome page"
def test_welcome_page(flask_app_client):
    response = flask_app_client.get('/welcome-page')
    assert b'Welcome to TUTOR TRACKER' in response.data

"Test for passing login"
def test_login_pass(flask_app_client):
    client = flask_app_client
    return client.post('/login' , data=dict(
        username='Lect1',password='123456'),follow_redirects=True)
    #assert request.status_code == 200

"Test for failing login: password not inputted"
def test_login_password_fail(flask_app_client):
    client = flask_app_client
    request = client.post('/login' , data=dict(
        username='Lect1',password=''),follow_redirects=True)
    assert request.status_code == 200

"Test for failing login: username not inputted"
def test_login_username_fail(flask_app_client):
    client = flask_app_client
    request = client.post('/login' , data=dict(
        username='',password='123456'),follow_redirects=True)
    assert request.status_code == 200

"Test for failing login: both details missing"
def test_login_both_fail(flask_app_client):
    client = flask_app_client
    request = client.post('/login' , data=dict(
        username='',password=''),follow_redirects=True)
    assert request.status_code == 200

"Test if the home route is working"
def test_lecturer_homepage(flask_app_client):
    client = flask_app_client
    request = client.get('/lecturer/home',follow_redirects=True)
    assert request.status_code == 200

"Test if the profile route is working"
def test_lecturer_profile(flask_app_client):
    client = flask_app_client
    request = client.get('/lecturer/profile',follow_redirects=True)
    assert request.status_code == 200   

"Test if registration is working"
def test_lecturer_registration(flask_app_client):
    client = flask_app_client
    request = client.post('/lecturer/registration', data=dict(
        firstname = 'Steve',
        lastname = 'James',
        email = 'steve@wits.ac.za',
        username = 'steve',
        employee_number = '100112',
        password1 = 'I am steve',
        password2 = 'I am steve', follow_redirected=True))
    assert request.status_code == 200
    
"Check if lecturer can edit profile unsuccessfully (failure)"
def test_lecturer_profile_edit(flask_app_client):
    client = flask_app_client
    request = client.post('lecturer/edit-profile', data= dict(
        office_number = 'WSS201',
        telephone_number = '07107107', follow_redirects = True))
    assert request.status_code == 302    

"Test lecturer registration with missing fields"
def test_lecturer_registration_failure(flask_app_client):
    client = flask_app_client
    request = client.post('/lecturer/registration', data=dict(
        firstname = 'Steve',
        lastname = 'James',
        username = 'steve',
        employee_number = '100112',
        password2 = 'I am steved', follow_redirected=True))
    assert request.status_code == 200

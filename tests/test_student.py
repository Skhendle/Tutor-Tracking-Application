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

    
def test_counter_login_username(flask_app_client):
    client = flask_app_client
    request = client.post('/login' , data=dict(
        username='',password='123456'),follow_redirects=True)
    assert request.status_code == 200

def test_counter_login_username_and_password(flask_app_client):
    client = flask_app_client
    request = client.post('/login' , data=dict(
        username='',password=''),follow_redirects=True)
    assert request.status_code == 200

def test_student_homepage(flask_app_client):
    client = flask_app_client
    request = client.get('/student/home',follow_redirects=True)
    assert request.status_code == 200

def test_student_profile(flask_app_client):
    client = flask_app_client
    request = client.get('/student/profile',follow_redirects=True)
    assert request.status_code == 200
    
def test_student_logout(flask_app_client):
    client = flask_app_client
    request = client.get('/logout',follow_redirects=True)
    assert request.status_code == 200

def test_student_registration(flask_app_client):
    client = flask_app_client
    request = client.post('/lecturer/registration', data=dict(
        firstname = 'Senza',
        lastname = 'Mamba',
        email = '666333222@students.ac.za',
        username = 'Senza',
        year_of_study = 2,  
        student_number = '6663322',
        password1 = '12345678',
        password2 = '12345678', follow_redirected=True))
    assert request.status_code == 200
    

def test_additional_student_registration(flask_app_client):
    client = flask_app_client
    request = client.post('/student/registration', data=dict(
        firstname = 'Sihle',
        lastname = 'Majola',
        username = 'sj_majola',
        year_of_study = 4,
        email = "sj@gmail.com",
        student_number = '66554422',
        password2 = '12345678', follow_redirected=True))
    assert request.status_code == 200

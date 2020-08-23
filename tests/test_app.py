import os
import tempfile

import pytest
import app
from app import app, tutortracker, db

@pytest.fixture
def client():
	db_fd, tutortracker.app.config['DATABASE'] = tempfile.mkstemp()
	tutortracker.app.config['TESTING'] = True

	with tutortracker.app.test_client() as client:
		with app.app_context():
			app.make_shell_context()
		yield client

	os.close(db_fd)
	os.unlink(tutortracker.app.config['DATABASE'])

def login(client, username, password):
    return client.post('/login', data=dict(
        username=username,
        password=password
    ), follow_redirects=True)
"""
def registration_tutor(client, firstname, lastname, username, email, student_number, year_of_study, password):
    return client.post('/tutor/registration', data=dict(
		
        username=username,
        password=password
    ), follow_redirects=True)
"""
def logout(client):
    return client.get('/logout', follow_redirects=True)

"""Checking if we can post a valid login"""
def test_login_post(client):
	assert login(client, '12345', 'password').status_code == 200

"""Checking if we can post an invalid login and get a fail code"""
def test_login_post_invalid(client):
	print(str(login(client, '', 'password').status_code))
	assert login(client, '', 'password').status_code == 200

"""Checking if we can post a valid logout"""
def test_logout_post(client):
	assert logout(client).status_code == 200

"""Checking if the app opens the indeex page"""
def test_index_page(client):
	rv = client.get('/')
	assert b'Welcome to TUTOR TRACKER' in rv.data	

"""Checking if the app opens the indeex page"""
def test_loggin_page(client):
	rv = client.get('/login')
	assert b'New at TUTOR TRACKER?' in rv.data

"""Checking if the login button in the index page works"""
def test_index_to_login(client):
	client.get('/')
	rv = client.post('/login')
	assert b'New at TUTOR TRACKER?' in rv.data

"""Checking if the tutor registraation form exists page works"""
def test_tutor_registration(client):
	rv = client.get('/tutor/registration')
	assert b'Create your student account' in rv.data

	
"""Checking if the tutor registraation form exists page works"""
def test_lecture_registration(client):
	rv = client.get('/lecture/registration')
	assert b'Create your lecture account' in rv.data

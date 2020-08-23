import os
import tempfile

import pytest
import app
from app import app, tutortracker, db

def login(client, username, password):
    return client.post('/login', data=dict(
        username=username,
        password=password
    ), follow_redirects=True)

def logout(client):
    return client.get('/logout', follow_redirects=True)


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
	login(client, '12345', 'password')


def test_index_page(client):
	"""Checking if the app opens the indeex page"""

	rv = client.get('/')
	assert b'Welcome to TUTOR TRACKER' in rv.data

def test_loggin_page(client):
	"""Checking if the app opens the indeex page"""

	rv = client.get('/login')
	assert b'New at TUTOR TRACKER?' in rv.data



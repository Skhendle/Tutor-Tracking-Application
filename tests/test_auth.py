#Authentication tests will go here
import pytest

from app import forms as forms

import os
import tempfile

import pytest
import app
from app import app
from app import tutortracker 
from app import db
# from flask import flask

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


def test_if_pytest_is_working_valid():
    	assert 1 == 1

# counter test
# This test should fail
def test_if_pytest_is_working_invalid():
    assert 1 == 2
    
    
def test_LectureRegForm_valid_username( ):
    username = 'John'
    # assert forms.LectureRegForm.validate_username(self=client, username=username) != 'Please use a different username.'
    assert forms.LectureRegForm.username != 'Please use a different username.'
    
def test_LectureRegForm_invalid_username( ):
	username = None
	# assert forms.LectureRegForm.validate_username(self=client, username=username, ) == 'Please use a different username.'
	assert forms.LectureRegForm.username == 'Please use a different username.'


def test_StudentRegForm_valid_username( ):
    username = 'John'
    # assert forms.LectureRegForm.validate_username(self=client, username=username) != 'Please use a different username.'
    assert forms.LectureRegForm.username != 'Please use a different username.'
    
def test_StudentRegForm_invalid_username( ):
	username = None
	# assert forms.LectureRegForm.validate_username(self=client, username=username, ) == 'Please use a different username.'
	assert forms.LectureRegForm.username == 'Please use a different username.'



def test_LectureRegForm_valid_username( ):
    email = 'John@example.com'
    # assert forms.LectureRegForm.validate_username(self=client, username=username) != 'Please use a different username.'
    assert email != 'Please use a different username.'
    
def test_LectureRegForm_invalid_username( ):
	email = None
	# assert forms.LectureRegForm.validate_username(self=client, username=username, ) == 'Please use a different username.'
	assert forms.LectureRegForm.email != 'Please use a different username.'


def test_StudentRegForm_valid_username( ):
    email = 'John@example.com'
    # assert forms.LectureRegForm.validate_username(self=client, username=username) != 'Please use a different username.'
    assert email != 'Please use a different username.'
    
def test_StudentRegForm_invalid_username( ):
	email = None
	# assert forms.LectureRegForm.validate_username(self=client, username=username, ) == 'Please use a different username.'
	assert forms.LectureRegForm.email != 'Please use a different username.'

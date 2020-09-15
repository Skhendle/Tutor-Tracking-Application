import pytest
from flask import url_for


"""So far: Testing if the course routes are working
create_course - is the course creation process working

"""


"Test if create course route by lecturer is working"
def test_create_course(flask_app_client):
    client = flask_app_client
    request = client.get('/courses/create-course',follow_redirects=True)
    assert request.status_code == 200 

"Test if course session creation by lecturer route is working"
def test_tutorial_session_course(flask_app_client):
    client = flask_app_client
    request = client.get('/courses/create_session',follow_redirects=True)
    assert request.status_code == 200

"Test if the view session by totor route is working"
def test_view_course_session(flask_app_client):
    client = flask_app_client
    request = client.get('/courses/view_session_tutor',follow_redirects=True)
    assert request.status_code == 200

"test tutorial session creation by lecturer"
def test_session_creation(flask_app_client):
    client = flask_app_client
    request = client.post('/courses/create_session', data = dict(
        course_code = 'Coms3001',
        name = 'SomethingComs',
        venue = 'MSL001',
        start_time = '14:55:00',
        end_time = '15:30:00',
        day = '12.10.2020',
        key = '300400555',
        number_of_tutors = '6',
        lecturer = 'steve',
        course_lecturer = 'steve', follow_redirects = True))
    assert request.status_code != 200


""" Use this template for testing routes. routes are the easiest to test for

def test_create_course(flask_app_client):
    client = flask_app_client
    request = client.get('/courses/create-course',follow_redirects=True)
    assert request.status_code == 200 
"""
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
        follow_redirects = True))
    assert request.status_code != 200


"Test if the view session by totor route is working"
def test_view_my_courses(flask_app_client):
    client = flask_app_client
    request = client.get('courses/my-courses',follow_redirects=True)
    assert request.status_code == 200

"Test if the view explore by totor route is working"
def test_view_explore(flask_app_client):
    client = flask_app_client
    request = client.get('courses/explore',follow_redirects=True)
    assert request.status_code == 200

    "Test if the view apply by totor route is working"
def test_view_apply(flask_app_client):
    client = flask_app_client
    request = client.get('courses/apply',follow_redirects=True)
    assert request.status_code == 200

    "Test if the view show_course_details by totor route is working"
def test_view_my_courses(flask_app_client):
    client = flask_app_client
    request = client.get('courses/<course_code>',follow_redirects=True)
    assert request.status_code == 200

    "Test if the view enroll by totor route is working"
def test_enroll(flask_app_client):
    client = flask_app_client
    request = client.post('/courses/enroll/<course_code>', data = dict(
        course_code = 'coms2004',
        follow_redirects = True))
    assert request.status_code != 200

    "test edit course details by lecturer"
def test_edit_profile(flask_app_client):
    client = flask_app_client
    request = client.post('/course/<course_code>', data = dict(
        course_code = 'Coms2004',
        name = 'Mobile computing',
        venue = 'MSL004',
        start_time = '15:00:00',
        end_time = '16:30:00',
        day = '02.08.2020',
        number_of_tutors = '9',
        key = '38705000', follow_redirects = True))
    assert request.status_code != 200



    
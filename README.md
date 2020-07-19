[![Build Status](https://travis-ci.org/Skhendle/Tutor-Tracking-Application.svg?branch=master)](https://travis-ci.org/Skhendle/Tutor-Tracking-Application)
[![codecov](https://codecov.io/gh/Skhendle/Tutor-Tracking-Application/branch/master/graph/badge.svg)](https://codecov.io/gh/Skhendle/Tutor-Tracking-Application)

# Tutor Tracking Application

The tutor tracking website is an application to monitor tutor-related activity by lecturers mostly during Wits labs. The purpose of the application is to check tutor productivity. The website will have a lecture side and a tutor side.
## Features associated with the application:
### Lecturer’s side:
The lecturer can login as an administrator, and create a tutorial session that tutors can join
During a tutorial session created by the lecturer, they can then monitor the tutor’s activity such as time the tutor started the session and when the tutor ended the session, how many sessions the tutor has attended.
(Might be implemented) To keep the register the lecture will scan a QR code from each student to mark them as present.
### Tutor’s side:
The tutor can login as a student and join a tutorial session created by the lecturer using a unique code sent by the lecturer to them.
During a tutorial, the tutor can see the amount of time they have been present in the session, and they can also access their session history.
Can get an estimate of how much they made for their sessions overally.
On top of accessing their session history, the tutor can also view their upcoming tutorial sessions that have been created by their lecturer 
(Might be implemented) a unique QR code will be generated for each session so that the lecturer can scan it as proof of attendance.

### Additional features (both or neither the tutor’s side or lecturer’s side):
A tutor and/or a lecturer can see the payment history

# Project struture
[Link to the flask documentation file](https://flask.palletsprojects.com/en/1.1.x/tutorial/layout/)
## flaskr:
  * __init__.py 
    * Is the main file from which will be starting the app from
  * auth.py 
    * Is the file from which our login and register backend functionalities will be implented in for both lecturer and student.
  * lecturer.py
    * Is the file from which the backend functionality of the lecturer will be implemented.
  * student.py
    * Is the file from which the backend functionality of the student will be implemented.
  ### static:
    * style.css
      * The styling for the frontend
  ### templates: Contains the  html pages and folders with html pages for each use case in the project
  

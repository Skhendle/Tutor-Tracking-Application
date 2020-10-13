[![Build Status](https://travis-ci.org/Skhendle/Tutor-Tracking-Application.svg?branch=master)](https://travis-ci.org/Skhendle/Tutor-Tracking-Application)
[![codecov](https://codecov.io/gh/Skhendle/Tutor-Tracking-Application/branch/master/graph/badge.svg)](https://codecov.io/gh/Skhendle/Tutor-Tracking-Application)

# Tutor Tracking Application

The tutor tracking website is an application to monitor tutor-related activity by lecturers mostly during tutorial sessions. The purpose of the application is to check tutor productivity.

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

# Flow

![Image of architecture flow diagram](https://github.com/Skhendle/Tutor-Tracking-Application/blob/master/Documentation/flow.png)



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
  ### static: Front-end:
  * style.css
   * The styling for the frontend
  
  ### templates: Front-end 
   Contains the  html pages and folders with html pages for each use case in the project
   * auth
     - login.html
     - register.html
   * lecturer
     - main.html
   * student
     - main.html
   * base.html
   
 # Run Application Locally:
 
 
Clone the `Tutor Tracking` project locally. In a terminal, run:

```
$ git clone https://github.com/Skhendle/Tutor-Tracking-Application
```

Navigate into the cloned folder:
```
$ cd Tutor-Tracking-Application
```

Create a virtual environment inside the folder:
```
$ python3 -m venv venv
```

Activate the environment:
#### Windows:
```
$ venv\Scripts\activate
```
#### Unix:
```
$ . venv/bin/activate
```

Install Flask:
```
$ pip install Flask
```

You might need to install a few more dependencies before running the application, use:
```
$ pip install dependency-name  
```

Some of the few dependencies you will need:
```
$ pip install python-dotenv
$ pip install flask_sqlalchemy
$ pip install flask_migrate
$ pip install flask_login
$ pip install flask_wtf
$ pip install email_validator
```

Run the Application:
```
$ flask run
```


# Docker

## Install Docker: https://docs.docker.com/get-docker/

Docker is a platform for developers and sysadmins to build, run, and share applications with containers. The use of containers to deploy applications is called containerization. Containers are not new, but their use for easily deploying applications is.

Docker can build images automatically by reading the instructions from a Dockerfile. A Dockerfile is a text document that contains all the commands a user could call on the command line to assemble an image. Using docker build users can create an automated build that executes several command-line instructions in succession.

In the application file, we have created a Dockerfile

Build the Application:
```
$ docker build -t "tutortracker" 
```

The build is run by the Docker daemon, not by the CLI. The first thing a build process does is send the entire context (recursively) to the daemon. In most cases, it’s best to start with an empty directory as context and keep your Dockerfile in that directory. Add only the files needed for building the Dockerfile.

    Warning

    Do not use your root directory, /, as the PATH as it causes the build to transfer the entire contents of your hard drive to the Docker daemon.

'docker ps' is the essential command to list existing docker containers in running state. ps stands for “Process Status”. ps command is used to describe process status is Unix variants of operating systems and docker borrowed the naming convention from there.

List Current Existing docker containers:
```
$ docker ps 
```






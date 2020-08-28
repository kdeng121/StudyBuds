# StudyBuds - Webapp for Peer Learning

## Description
StudyBuds is a web application that allows users to create, view, and search study groups. It aims to make studying in college more interactive and fun! Developed in Python (Django) and uses a PostgreSQL database.

## Demo
https://studybuds.herokuapp.com/studygroups/

## To run locally:
0. Install django
1. Install postgres - [guide](https://www.techrepublic.com/blog/diy-it-guy/diy-a-postgresql-database-server-setup-anyone-can-handle/)
2. ~/mysite$ python3 manage.py makemigrations && python3 manage.py migrate
3. ~/mysite$ python3 manage.py runserver
4. visit `127.0.0.1:8000/studygroups`

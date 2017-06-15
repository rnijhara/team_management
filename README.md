# Team Management

## Steps:

* Create and activate virtualenv.
  `virtualenv env` 
  `source env/bin/activate`

* Install requirements.
  `pip install -r requirements.txt`
 
* Create new database with name "team_management_db" in MySQL.
  `create database team_management_db`
 
* Update database info in `team_management/team_management/settings.py`
`DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'team_management_db',
    'USER': 'DB_USER',
    'PASSWORD': 'DB_PASSWORD',
    'HOST': 'DB_HOST',
    'PORT': 'DB_PORT',
  }
}`
  
* In the project root, run migrations.
  `python manage.py migrate`
  
* Create superuser, give user_name, email and password when prompted.
  `python manage.py createsuperuser`

* Run the development server.
  `python manage.py runserver`

* Open the django admin portal http://127.0.0.1:8000/admin/ in your browser and login using the superuser credentials.

* Add the Team Member Roles for "admin" and "regular".

* Test the API by calling it as mentioned below.


# Calling the API

* List all Team Members:
  `curl -X GET "http://127.0.0.1:8000/team/"`
  
* Add a new Team Member:
  `curl -X POST -H "Content-Type: application/json" -d '{
    "first_name":"Roopak",
    "last_name":"Nijhara",
    "phone_number":"8869952780",
    "email":"roopaknijhara@gmail.com",
    "role": 1
  }' "http://127.0.0.1:8000/team/"`
  
* Update a Team Member:
  `curl -X PUT -H "Content-Type: application/json" -d '{
    "phone_number":"8869952785",
    "role": 2
  }' "http://127.0.0.1:8000/team/<id>/"`
 
* Delete a Team Member:
  `curl -X DELETE "http://127.0.0.1:8000/team/<id>/"`

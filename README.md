# python-tutorial


## python Commands

pip install requests -> Make request other microservices


python3 manage.py runserver 8001 -> runserver
python3 manage.py migrations -> run migrations before migrate to create in database
python3 manage.py migrate -> run migration in database to create the tables

## Environment setup 

django-admin startproject app . -> this command should be run into the project root folder to initialize the project "configuration folder".
django-admin startapp core -> this command should be run into the project root folder to create the core project "our business logic".
- add 'rest_framework' into app/settings INSTALLED_APPS section
- add 'corsheaders' into app/settings INSTALLED_APPS section
- add 'core' into app/settings INSTALLED_APPS section
- add 'corsheaders.middleware.CorsMiddleware' into app/settings MIDDLEWARE section before django....
- add 'CORS_ALLOW_ALL_ORIGINS = True' into app/settings as a constant

## Install Django 

### Create the project directory
mkdir tutorial
cd tutorial

### Create a virtual environment to isolate our package dependencies locally
python3 -m venv env
****** ONLY FOR WINDOWS //// source env/bin/activate  # On Windows use `env\Scripts\activate`

### Install Django and Django REST framework into the virtual environment
pip install django
pip install djangorestframework
pip install django-cors-headers -> reference: https://pypi.org/project/django-cors-headers/

# mysql commands 

mysql.server stop/start -> Run and stop mysql server
SET PASSWORD FOR 'root'@'localhost' = PASSWORD('new_password'); -> set password mysql


# references 

https://www.django-rest-framework.org/ -> django rest framework "Tutorial/Quick start"

https://www.youtube.com/watch?v=rOpJhKa-Chk&list=RDCMUCljAHzX-PBxv6WrXkI2rnQw&start_radio=1&rv=rOpJhKa-Chk&t=1344&ab_channel=ScalableScripts -> tutorial url

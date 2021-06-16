# Revaamp - Buy refurbished laptops online!

## Steps for initial setup:

 - python3 -m venv revaampvenv (create a venv)
 - source revaampvenv/bin/activate (activates venv)
 - pip3 install django
 - django-admin startproject revaamp
 - python3 manage.py runserver

## Migrations

 - python3 manage.py migrate

# Create a superuser to login to admin

 - python3 manage.py createsuperuser
 - (username, email, password)

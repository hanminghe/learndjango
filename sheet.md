# Django project commands

## after pip install django start a project
```
$ django-admin startproject mysite
```
## start a project inside a directory
```
$ django-admin startproject mysite .
```
## run project as a server
```
$ python manage.py runserver
```
## add a app to the project
```
$ python manage.py startapp blog
or
$ django-admin startapp blog
```
## after editting model run makemigrations
```
$ python manage.py makemigrations
```
## create superuser -- first user
```
$ python manage.py createsuperuser
```

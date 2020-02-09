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
## after editting model run makemigrations, must add app name to INSTALLED_APPS =[]
```
$ python manage.py makemigrations
```
## create superuser -- first user
```
$ python manage.py createsuperuser
```
https://www.cnblogs.com/zhuchenglin/p/9732245.html
https://www.cnblogs.com/zhuchenglin/p/10755547.html

在接收前端请求的文件中（我这边是view.py）中引入
from django.views.decorators.csrf import csrf_exempt
然后在每个不需要csrf验证的方法上方加上
@csrf_exempt
这样就可以了（或者是在settings文件中将csrf的中间件给注释掉也行）。

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

##nginx
```
    location /socket.io {
                proxy_pass http://127.0.0.1:888;
                proxy_http_version 1.1;
                proxy_set_header Host $host;
                proxy_set_header X-Real-IP $remote_addr;
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                
                proxy_set_header Upgrade $http_upgrade;
                proxy_set_header Connection "upgrade";
	}
 ```
##supervisord.d\1.ini
```
[program:app]
command=/run/quiz.sh
user=root
autorestart=true
startretires=3
redirect_stderr=true
stdout_logfile=/temp/super_log.txt
stderr_logfile=/temp/super_err.txt

 ```
 
 ##/run/quiz.sh
```
 #! /bin/bash
cd /quiz
source /venv/bin/activate
exec gunicorn -w 4 -b 127.0.0.1:888 --worker-class eventlet --log-level debug --capture-output --access-logfile /tmp/gunicorn-access.log --error-logfile /tmp/gunicorn-error.log -t 120 app:app
 ```
 Flask Gunicorn Supervisor Nginx 项目部署小总结 [link](https://gist.github.com/binderclip/f6b6f5ed4d71fa64c7c5#file-deploy-flask-gunicorn-supervisor-nginx-md)

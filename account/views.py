from django.shortcuts import render
from .form import LoginForm
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
# Create your views here.
def userlogin(request):
    if request.method=="GET":
        loginform=LoginForm()
        return render(request,"account/login.html",{"form":loginform})
    elif request.method=="POST":
        loginform=LoginForm(request.POST)
        if loginform.is_valid():
            cd=loginform.cleaned_data #without above line there was an error saying no attibute
            user=authenticate(username=cd['username'],password=cd['password'])
            if user:
                login(request,user)
                return HttpResponse("logged in")
            else:
                return HttpResponse("no authentication")

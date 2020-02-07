from django.shortcuts import render
from .form import LoginForm
# Create your views here.
def login(request):
    if request.method=="GET":
        loginform=LoginForm()
        return render(request,"account/login.html",{"form":loginform})

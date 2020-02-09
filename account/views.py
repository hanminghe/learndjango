from django.shortcuts import render
from .form import LoginForm, RegistrationForm, UserProfileForm
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

def userregister(request):
    if request.method=="GET":
        regform=RegistrationForm()
        profileform=UserProfileForm()
        return render(request,"account/register.html",{"form":regform,"profile":profileform})
    elif request.method=="POST":
        regform=RegistrationForm(request.POST)
        profileform=UserProfileForm(request.POST)
        if regform.is_valid():
            new_user=regform.save(commit=False)
            new_user.set_password(regform.cleaned_data['password'])
            new_user.save()
            new_profile=profileform.save(commit=False)
            new_profile.user=new_user
            new_profile.save()
            return HttpResponse("success")
        else:

            return HttpResponse(regform._errors)

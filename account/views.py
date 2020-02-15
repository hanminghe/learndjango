from django.shortcuts import render
from .form import LoginForm, RegistrationForm, UserProfileForm, UserForm, UserInfoForm
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from .models import UserProfile,UserInfo
from django.contrib.auth.models import User
from django.views.decorators.clickjacking import xframe_options_exempt

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

@login_required()
def myself(request):
    userprofile=UserProfile.objects.get(user=request.user) if \
                        hasattr(request.user,"userprofile") else \
                        UserProfile.objects.create(user=request.user)
    userinfo=UserInfo.objects.get(user=request.user) if \
                        hasattr(request.user,'userinfo') else \
                        UserInfo.objects.create(user=request.user)
    return render(request,"account/myself.html",
                    {"user":request.user,
                    "userinfo":userinfo,
                    "userprofile":userprofile})
@login_required()
def myself_edit(request):
    userprofile=UserProfile.objects.get(user=request.user) if \
                        hasattr(request.user,"userprofile") else \
                        UserProfile.objects.create(user=request.user)
    userinfo=UserInfo.objects.get(user=request.user) if \
                        hasattr(request.user,'userinfo') else \
                        UserInfo.objects.create(user=request.user)
    print(userinfo)
    if request.method == "POST":
        userform=UserForm(request.POST)
        userprofile_form=UserProfileForm(request.POST)
        userinfo_form=UserInfoForm(request.POST)
        if userform.is_valid() * userprofile_form.is_valid() * userinfo_form.is_valid():
            user_cd=userform.cleaned_data
            userprofile_cd=userprofile_form.cleaned_data
            userinfo_cd=userinfo_form.cleaned_data
            request.user.email=user_cd['email']
            userprofile.birth=userprofile_cd['birth']
            userprofile.phone=userprofile_cd['phone']
            userinfo.school=userinfo_cd['school']
            userinfo.company=userinfo_cd['company']
            userinfo.profession=userinfo_cd['profession']
            userinfo.address=userinfo_cd['address']
            userinfo.aboutme=userinfo_cd['aboutme']
            request.user.save()
            userprofile.save()
            userinfo.save()
        return HttpResponseRedirect('/account/my-information')
    else:
        user_form=UserForm(instance=request.user)
        userprofile_form=UserProfileForm(initial={
            "birth":userprofile.birth,
            "phone":userprofile.phone
        })
        userinfo_form=UserInfoForm(initial={
            "school":userinfo.school,
            "company":userinfo.company,
            "profession":userinfo.profession,
            "address":userinfo.address,
            "aboutme":userinfo.aboutme

        })

        return render(request,"account/myself_edit.html",
                    {"user_form":user_form,
                    "userinfo_form":userinfo_form,
                    "userprofile_form":userprofile_form})

@login_required()
@xframe_options_exempt
def my_image(request):
    if request.method =="GET":
        print(request.method)
        return render(request,'account/imagecrop.html')
    else:
        img=request.POST['img']
        print(img)
        userinfo=UserInfo.objects.filter(user=request.user.id).first()
        print(userinfo)
        if userinfo != None:
            userinfo.photo=img
            userinfo.save()
            return JsonResponse({'msg': 1})
        else:
            return JsonResponse({'msg': 0})

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # path('',views.userlogin,name='login'),
    path('login', auth_views.LoginView.as_view(template_name="account/login2.html"),name='login'),
    path('logout', auth_views.LogoutView.as_view(),name='logout')

]

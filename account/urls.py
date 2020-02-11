from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # path('',views.userlogin,name='login'),
    path('login', auth_views.LoginView.as_view(template_name="account/login2.html"),name='login'),
    path('logout', auth_views.LogoutView.as_view(),name='logout'),
    path('register', views.userregister,name='register'),
    path('password-change', auth_views.PasswordChangeView.as_view(
        template_name="account/password_change_form.html",
        success_url="/account/password-change-done"),
        name='password-change'),
    path('password-change-done', auth_views.PasswordChangeDoneView.as_view(
        template_name="account/password_change_done.html"),
        name='password-change-done'),

]

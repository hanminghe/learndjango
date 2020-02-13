from django.urls import path ,reverse_lazy
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # path('',views.userlogin,name='login'),
    path('login', auth_views.LoginView.as_view(template_name="account/login2.html"),name='login'),
    path('logout', auth_views.LogoutView.as_view(),name='logout'),
    path('register', views.userregister,name='register'),
    path('password-change', auth_views.PasswordChangeView.as_view(
        template_name="account/password_change_form.html",
        success_url=reverse_lazy('account:password-change-done')),
        name='password-change'),
    path('password-change-done', auth_views.PasswordChangeDoneView.as_view(
        template_name="account/password_change_done.html"),
        name='password-change-done'),
    path('password-reset', auth_views.PasswordResetView.as_view(
        template_name="account/password_reset_form.html",
        email_template_name="account/password_reset_email.html",
        success_url="/account/password-reset-done"),
        name='password-reset'),
    path('password-reset-done',auth_views.PasswordResetDoneView.as_view(
        template_name="account/password_reset_done.html"),
        name="password-reset-done"),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name="account/password_reset_confirm.html",
        success_url="/account/password-reset-complete/"),
        name='password-reset-confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name="account/password_reset_complete.html"),
        name='password-reset-complete'),
    path('my-information',views.myself,name="my-information"),
    
]

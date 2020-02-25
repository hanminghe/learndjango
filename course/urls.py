from django.urls import path
from . import views

app_name="course"

urlpatterns=[
    path('about/',views.AboutView.as_view(),name="about"),
]

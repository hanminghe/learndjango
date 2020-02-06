from django.urls import path
from . import views

urlpatterns = [
    path('',views.blog_title),
    path('<int:id>',views.blog_content),
]

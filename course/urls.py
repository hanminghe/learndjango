from django.urls import path
from . import views

app_name="course"

urlpatterns=[
    path('about/',views.AboutView.as_view(),name="about"),
    path('course-list/',views.CourseListView.as_view(),name="course-list"),
    path('manage-course/',views.ManageCourseListView.as_view(),name="manage-course"),
]

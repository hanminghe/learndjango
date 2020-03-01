from django.urls import path
from . import views

app_name="course"

urlpatterns=[
    path('about/',views.AboutView.as_view(),name="about"),
    path('course-list/',views.CourseListView.as_view(),name="course-list"),
    path('manage-course/',views.ManageCourseListView.as_view(),name="manage-course"),
    path('create-course/',views.CreateCourseView.as_view(),name="create-course"),
    path('delete-course/<int:pk>',views.DeleteCourseView.as_view(),name="delete-course"),
    path('edit-course/<int:pk>',views.UpdateCourseView.as_view(),name="edit-course"),
    path('create-lesson/',views.CreateLessonView.as_view(),name='create-lesson'),
    path('lesson-list/',views.LessonListView.as_view(),name="lesson-list"),
]

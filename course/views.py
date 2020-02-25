from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.
from django.views.generic import TemplateView,ListView
from .models import Course

class AboutView(TemplateView):
    template_name="course/about.html"

class CourseListView(ListView):
    model=Course  # equal to Course.objects.all()
    # queryset=Course.objects.filter(id = 1)   # one method
    # user=User.objects.filter(username = "")

    context_object_name="courses"  # param  name of inside tempalte
    template_name="course/course_list.html"

    def get_queryset(self):
        qs=super(CourseListView,self).get_queryset()
        return qs.filter(id = 1)

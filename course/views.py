from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import TemplateView,ListView,CreateView,DeleteView,UpdateView
from .models import Course
from django import forms
import json
from django.http import HttpResponse


class CreateCourseForm(forms.ModelForm):
    class Meta:
        model=Course
        fields=("title","overview")

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

class UserMixin:
    def get_queryset(self):
        qs=super(UserMixin,self).get_queryset()
        return qs.filter(user=self.request.user)

from braces.views import LoginRequiredMixin

class UserCourseMixin(UserMixin,LoginRequiredMixin):
    model=Course


class ManageCourseListView(UserCourseMixin,ListView):
    context_object_name="courses"
    template_name="course/manage_course_list.html"

class CreateCourseView(UserCourseMixin,CreateView):
    fields=['title','overview']
    template_name='course/create_course.html'

    def post(self,request,*args,**kargs):
        form=CreateCourseForm(data=request.POST)
        if form.is_valid():
            new_course=form.save(commit=False)
            new_course.user=self.request.user
            new_course.save()
            return redirect("course:manage-course")
        return self.render_to_response({"form":form})

class UpdateCourseView(UserCourseMixin,UpdateView):
    fields=['id','title','overview']
    template_name='course/edit_course.html'
    success_url = reverse_lazy("course:manage-course")



class DeleteCourseView(UserCourseMixin, DeleteView):
    template_name = 'course/delete_course.html'
    success_url = reverse_lazy("course:manage-course")

    def dispatch(self, *args, **kwargs):
        resp = super(DeleteCourseView, self).dispatch(*args, **kwargs)
        if self.request.is_ajax():
            response_data = {"result": "ok"}
            return HttpResponse(json.dumps(response_data), content_type="application/json")
        else:
            return resp

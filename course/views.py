from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import View, TemplateView,ListView,CreateView,DeleteView,UpdateView
from django.views.generic.base import TemplateResponseMixin
from .models import Course,Lesson
from django import forms
import json
from django.http import HttpResponse


class CreateCourseForm(forms.ModelForm):
    class Meta:
        model=Course
        fields=("title","overview")

class CreateLessonForm(forms.ModelForm):
    class Meta:
        model=Lesson
        fields=['course','title','video','description','attach']

    def __init__(self,user,*args,**kargs):
        super(CreateLessonForm,self).__init__(*args,**kargs)
        self.fields['course'].queryset=Course.objects.filter(user=user)


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

class CreateLessonView(LoginRequiredMixin,CreateView):
    model= Lesson
    login_url="/account/login"

    def get(self,request,*args,**kargs):
        form=CreateLessonForm(user=self.request.user)
        return render(request,"course/create_lesson.html",{"form":form})

    def post(self,request,*args,**kargs):
        form=CreateLessonForm(self.request.user,request.POST,request.FILES)
        if form.is_valid():
            new_lesson=form.save(commit=False)
            new_lesson.user=self.request.user
            new_lesson.save()
            return redirect("course:manage-course")




class LessonListView(ListView):
    model=Lesson  # equal to Course.objects.all()


    context_object_name="lessons"  # param  name of inside tempalte
    template_name="course/lesson_list.html"

    def get_queryset(self):
        qs=super(LessonListView,self).get_queryset()
        return qs

class ListLessonView(LoginRequiredMixin,TemplateResponseMixin,View):
    template_name="course/list_lesson.html"

    def get(self,request,course_id):
        course=get_object_or_404(Course,id=course_id)
        return self.render_to_response({'course':course})

class DetailLessonView(LoginRequiredMixin,TemplateResponseMixin,View):
    login_url="account/login/"
    template_name="course/detail_lesson.html"

    def get(self,request,lesson_id):
        lesson=get_object_or_404(Lesson,id=lesson_id)
        return self.render_to_response({"lesson":lesson})
        

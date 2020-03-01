from django.db import models
from slugify import slugify
from .fields import OrderField
# Create your models here.
from django.contrib.auth.models import User

class Course(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='courses_user')
    title = models.CharField( max_length=100)
    slug = models.SlugField(max_length=200,unique=True)
    overview = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=("-created",)

    def save(self,*args,**kargs):
        self.slug=slugify(self.title)
        super(Course,self).save(*args,**kargs)

    def __str__(self):
        return self.title

def user_derectory_path(instance,filename):
    return "courses/user_{0}/{1}".format(instance.user.id,filename)

class Lesson(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='lession_user')
    course=models.ForeignKey(Course,on_delete=models.CASCADE,related_name="lesson")
    title = models.CharField( max_length=200)
    video = models.FileField(upload_to=user_derectory_path)
    description = models.TextField(blank=True)
    attach = models.FileField(upload_to=user_derectory_path)
    created = models.DateTimeField(auto_now_add=True)
    order=OrderField(blank=True,for_fields=['course'])

    class Meta:
        ordering=['order']

    def __str__(self):
        return '{}.{}'.format(self.order,self.title)

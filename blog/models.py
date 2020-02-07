from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class BlogArticles(models.Model):
    title=models.CharField(max_length=255)
    author=models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    body=models.TextField()
    publish=models.DateTimeField(default=timezone.now)

    class Meta:
        ordering=("-publish",)

    def __str__(self):
        return self.title

# Create your models here.
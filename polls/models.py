from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Polls(models.Model):
    title=models.CharField(max_length=300)
    request_by=models.ForeignKey(User, on_delete=models.CASCADE,related_name="polls_name")
    body=models.TextField()
    publish=models.DateTimeField(default=timezone.now)

    class Meta:
        ordering=("-publish",)

    def __str__(self):
        return self.title

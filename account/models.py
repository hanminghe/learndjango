from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE,unique=True)
    birth=models.DateField(null=True, blank=True)
    phone=models.CharField(max_length=20,null=True)

    def __str__(self):
        return 'user {}'.format(self.user.username)

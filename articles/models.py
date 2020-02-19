from django.db import models
from django.contrib.auth.models import user

# Create your models here.
class AticleColumn(models.Model):
    user=models.ForeignKey(User,on_delete=CASCADE,related_name='article_column')
    column=models.CharField(max_length=200)
    created=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.column

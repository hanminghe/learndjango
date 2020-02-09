from django.contrib import admin
from .models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display=("user","birth","phone")
    list_filter=("phone",)
    search_fields=("phone",)
    ordering=['user']
admin.site.register(UserProfile, UserProfileAdmin)
# Register your models here.

from django.conf.urls import url
from . import views


app_name="image"

urlpatterns = [
    url('list-images/', views.list_images, name="list_images"),
    url('upload-image/', views.upload_image, name='upload_image'),
    url('del-image/', views.del_image, name='del_image'),
    url('images/', views.falls_images, name="falls_images"),
]

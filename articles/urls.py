from django.urls import path
from . import views

app_name="article"

urlpatterns = [
    path('article-column',views.article_column,name='article-column'),
    path('edit-article-column',views.edit_article_column,name='edit-article-column'),
    path('del-article-column',views.del_article_column,name='del-article-column'),
]

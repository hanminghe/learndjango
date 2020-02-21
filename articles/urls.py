from django.urls import path,re_path
from . import views

app_name="article"

urlpatterns = [
    path('article-column',views.article_column,name='article-column'),
    path('edit-article-column',views.edit_article_column,name='edit-article-column'),

    path('article-post',views.article_post,name='article-post'),
    path('article-list',views.article_list,name='article-list'),
    re_path('article-detail/(?P<id>\d+)/(?P<slug>[-\w]+)/$',views.article_detail,name='article_detail'),
    path('del-article',views.del_article,name='del-article'),
]

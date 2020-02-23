from django.urls import path,re_path
from . import views ,list_views

app_name="article"

urlpatterns = [
    path('article-column',views.article_column,name='article-column'),
    path('edit-article-column',views.edit_article_column,name='edit-article-column'),
    path('del-article-column',views.del_article_column,name='del-article-column'),
    path('article-post/<int:article_id>',views.article_post,name='article-post'),
    path('article-post',views.article_post,name='article-post'),
    path('article-list',views.article_list,name='article-list'),
    re_path('article-detail/(?P<id>\d+)/(?P<slug>[-\w]+)/$',views.article_detail,name='article_detail'),
    path('del-article',views.del_article,name='del-article'),
    path('article-list-all',list_views.article_list,name='article-list-all'),
    path('article-detail-all/<int:id>/<slug:slug>',list_views.article_detail,name='article-detail-all'),
]

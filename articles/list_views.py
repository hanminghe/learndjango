from django.shortcuts import render,get_object_or_404
from .models import ArticlePost
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.contrib.auth.models import User

def article_list(request,username=None):
    if username:
        user=User.objects.get(username=username)
        articles=ArticlePost.objects.filter(author=user)
    else:
        articles=ArticlePost.objects.all()
    paginator=Paginator(articles,3)
    page=request.GET.get('page')
    try:
        current_page=paginator.page(page)
    except PageNotAnInteger:
        current_page=paginator.page(1)
    except EmptyPage:
        current_page=paginator.page(paginator.num_pages)
    articles=current_page.object_list
    return render(request,"article/article_list_all.html",{"articles":articles,"page":current_page})

def article_detail(request,id,slug):
    article=get_object_or_404(ArticlePost,id=id,slug=slug)
    return render(request,"article/article_detail.html",{"article":article})

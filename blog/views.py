from django.shortcuts import render, get_object_or_404
from .models import BlogArticles

# Create your views here.

def blog_title(request):
    blogs=BlogArticles.objects.all()
    return render(request,"blog/blogs.html",{'blogs':blogs})

def blog_content(request,id):
    # article=BlogArticles.objects.get(id=id)
    article = get_object_or_404(BlogArticles,id=id)
    return render(request,"blog/content.html",{"article":article,"publish":article.publish})

from django.shortcuts import render,get_object_or_404
from .models import ArticlePost
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

def article_list(request,username=None):
    if username:
        user=User.objects.get(username=username)
        articles=ArticlePost.objects.filter(author=user)
        try:
            userinfo=user.userinfo
        except:
            userinfo=None
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
    if username:
        return render(request,"article/author_article_list.html",{"articles":articles,"page":current_page,"user":user,"userinfo":userinfo})
    else:
        return render(request,"article/article_list_all.html",{"articles":articles,"page":current_page})

def article_detail(request,id,slug):
    article=get_object_or_404(ArticlePost,id=id,slug=slug)
    return render(request,"article/article_detail.html",{"article":article})

@csrf_exempt
@require_POST
@login_required
def like_article(request):
    article_id=request.POST.get("id")
    action=request.POST.get("action")
    import traceback
    if article_id and action:
        try:
            article=ArticlePost.objects.get(id=article_id)
            if action=="like":
                article.users_like.add(request.user)
                return JsonResponse({'msg': 1,'notice':'liked'})
            else:
                article.users_like.remove(request.user)
                return JsonResponse({'msg': 2,'notice':'like removed'})
        except:
            traceback.print_exc()
            return JsonResponse({'msg': 0,'notice':'error'})

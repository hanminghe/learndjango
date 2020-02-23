from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import ArticleColumn,ArticlePost

from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.http import HttpResponse,JsonResponse
from .form import ArticleColumnForm,ArticlePostForm

from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

@login_required()
@csrf_exempt
def article_column(request):
    if request.method  == "GET":
        columns=ArticleColumn.objects.filter(user=request.user)
        column_form=ArticleColumnForm()
        return render(request,"article/article_column.html",{"columns":columns,"column_form":column_form})
    if request.method =="POST":
        column_name=request.POST['column']
        columns=ArticleColumn.objects.filter(user_id=request.user.id,column=column_name)
        if columns:
            return JsonResponse({'msg': 0,'notice':'the name provided was existing before'})

        else:
            ArticleColumn.objects.create(user=request.user,column=column_name)
            return JsonResponse({'msg': 1,'notice':'saved ok'})

@login_required()
@require_POST
@csrf_exempt
def edit_article_column(request):
        column_name=request.POST['column']
        id=request.POST['id']
        columns=ArticleColumn.objects.filter(user_id=request.user.id,id=id).get()
        if columns:
            columns.column=column_name
            columns.save()

            return JsonResponse({'msg': 1,'notice':'new column name saved'})

        else:

            return JsonResponse({'msg': 0,'notice':'nothing to edit'})

@login_required()
@require_POST
@csrf_exempt
def del_article_column(request):
        id=request.POST['id']
        columns=ArticleColumn.objects.filter(user_id=request.user.id,id=id).get()
        if columns:
            columns.delete()
            return JsonResponse({'msg': 1,'notice':'the column has been deleted'})
        else:
            return JsonResponse({'msg': 0,'notice':'nothing to delete'})

@login_required()
@csrf_exempt
def article_post(request,article_id=None):
    if request.method  == "GET":

        article_columns=request.user.article_column.all()
        if article_id ==None:
            post_form=ArticlePostForm()
            return render(request,"article/article_post.html",{"post_form":post_form,"article_columns":article_columns})
        else:
            article=ArticlePost.objects.get(id=article_id)
            post_form=ArticlePostForm(initial={"title":article.title})
            return render(request,"article/article_post.html",\
                    {"post_form":post_form,"article_columns":article_columns,\
                    "the_column":article.column,"article":article})

    if request.method =="POST":
        post_form=ArticlePostForm(data=request.POST)
        print(request.POST)
        if post_form.is_valid():
            cd=post_form.cleaned_data
            print(cd)
            import traceback
            try:
                if request.POST['article_id'] =='0':

                    new_post=post_form.save(commit=False)
                    new_post.author=request.user
                    new_post.column=request.user.article_column.get(id=request.POST['column_id'])
                    new_post.save()
                    return JsonResponse({'msg': 1,'notice':'new post was saved'})
                else:
                    article=ArticlePost.objects.get(id=request.POST['article_id'])
                    print(article)
                    article.title=request.POST['title']
                    article.body=request.POST['body']
                    article.column=request.user.article_column.get(id=request.POST['column_id'])
                    article.save()
                    return JsonResponse({'msg': 1,'notice':'post was updated'})
            except:
                traceback.print_exc()
                return JsonResponse({'msg': 0,'notice':'during save there was an error'})

        else:

            return JsonResponse({'msg': 2,'notice':'post data was unclean'})

@login_required
def article_list(request):
    articles=ArticlePost.objects.filter(author=request.user)
    paginator=Paginator(articles,2)
    page=request.GET.get('page')
    try:
        current_page=paginator.page(page)
    except PageNotAnInteger:
        current_page=paginator.page(1)
    except EmptyPage:
        current_page=paginator.page(paginator.num_pages)
    articles=current_page.object_list
    return render(request,"article/article_list.html",{"articles":articles,"page":current_page})

@login_required
def article_detail(request,id,slug):
    article=get_object_or_404(ArticlePost,id=id,slug=slug)
    article.users_view=article.users_view+1
    article.save()
    return render(request,"article/article_detail.html",{"article":article})

@login_required()
@require_POST
@csrf_exempt
def del_article(request):
        id=request.POST['id']
        post=ArticlePost.objects.filter(author=request.user.id,id=id).get()
        if post:
            post.delete()
            return JsonResponse({'msg': 1,'notice':'the post has been deleted'})
        else:
            return JsonResponse({'msg': 0,'notice':'nothing to delete'})

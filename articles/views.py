from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import ArticleColumn,ArticlePost

from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.http import HttpResponse,JsonResponse
from .form import ArticleColumnForm,ArticlePostForm

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
def article_post(request):
    if request.method  == "GET":
        article_columns=request.user.article_column.all()
        post_form=ArticlePostForm()
        return render(request,"article/article_post.html",{"post_form":post_form,"article_columns":article_columns})
    if request.method =="POST":
        post_form=ArticlePostForm(data=request.POST)
        print(request.POST)
        if post_form.is_valid():
            cd=post_form.cleaned_data
            print(cd)
            import traceback
            try:
                new_post=post_form.save(commit=False)
                new_post.author=request.user
                new_post.column=request.user.article_column.get(id=request.POST['id'])
                new_post.save()
                return JsonResponse({'msg': 1,'notice':'new post was saved'})
            except:
                traceback.print_exc()
                return JsonResponse({'msg': 0,'notice':'during save there was an error'})

        else:

            return JsonResponse({'msg': 2,'notice':'post data was unclean'})

@login_required
def article_list(request):
    articles=ArticlePost.objects.filter(author=request.user)
    return render(request,"article/article_list.html",{"articles":articles})

@login_required
def article_detail(request,id,slug):
    article=get_object_or_404(ArticlePost,id=id,slug=slug)
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

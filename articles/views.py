from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import ArticleColumn

from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.http import HttpResponse,JsonResponse
from .form import ArticleColumnForm

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
        article_post=request.user.article_column.all()
        post_form=ArticlePostForm()
        return render(request,"article/article_post.html",{"post_form":post_form,"article_post":article_post})
    if request.method =="POST":
        post_form=ArticlePostForm(data=request.POST)
        if post_form.is_valid():
            cd=post_form.cleaned_data
            try:
                new_post=post_form.save(commit=False)
                new_post.author=request.user
                new_post.column=request.user.article_column.get(id=request.POST['column_id'])
                new_post.save()
                return JsonResponse({'msg': 1,'notice':'new post was saved'})
            except:
                return JsonResponse({'msg': 0,'notice':'during save there was an error'})

        else:

            return JsonResponse({'msg': 2,'notice':'post data was unclean'})

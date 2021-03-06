from django import template

register = template.Library()

from ..models import ArticlePost

@register.simple_tag
def total_articles():
    return ArticlePost.objects.count()


@register.simple_tag
def author_total_articles(user):
    return user.PostBy.count() #PostBy is the related name of ForeignKey in ArticlePost mode

@register.inclusion_tag('article/latest_articles.html')
def latest_articles(n=5):
    latest_articles=ArticlePost.objects.order_by("-created")[:n]
    return {"latest_articles":latest_articles}

from django.db.models import Count
@register.simple_tag
def most_commented_articles(n=3):
    return ArticlePost.objects.annotate(total_comments=Count('comment')).order_by("-total_comments")[:n]

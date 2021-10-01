from django.http.response import HttpResponse
from django.shortcuts import render,HttpResponse
from . import models

def articles_list(request):
    articles = models.Article.objects.all().order_by('date')
    return render(request, 'articles/articleslist.html', {'articles': articles})

def article_detail(request,slug):
    return HttpResponse(slug)
    
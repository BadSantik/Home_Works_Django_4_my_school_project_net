from django.shortcuts import render
from django.views.generic import ListView
from .models import Article


class ArticleListView(ListView):
    model = Article
    template_name = 'news.html'
    context_object_name = 'object_list'


def home(request):
    return render(request, 'home.html')

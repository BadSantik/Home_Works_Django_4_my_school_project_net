from django.urls import path
from .views import ArticleListView, home

urlpatterns = [
    path('', home, name='home'),
    path('articles/', ArticleListView.as_view(), name='article-list'),
]

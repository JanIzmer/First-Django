from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_home, name='news_home'),
    path('create', views.create, name='create'),
    path('user_articles', views.user_articles, name='user_articles'),
    path('<int:pk>', views.NewsDetailView.as_view(), name='news-detail'),
    path('<int:pk>/update', views.NewsUpdateView.as_view(), name='wiew-update'),
    path('<int:pk>/delete', views.NewsDeleteView.as_view(), name='wiew-delete'),
]
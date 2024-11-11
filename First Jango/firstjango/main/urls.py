from django.urls import path
from . import views
from .views import RegisterView
urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('profile', views.profile_view, name='profile'),
    path('register', RegisterView.as_view(), name='register'),

]
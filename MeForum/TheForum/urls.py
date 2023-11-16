from django.urls import path
#from . import views
from .views import HomeView, ArticleDetailVIew

urlpatterns = [
    #path('', views.home, name="home"),
    path('',  HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetailVIew.as_view(), name='article-details'),
]

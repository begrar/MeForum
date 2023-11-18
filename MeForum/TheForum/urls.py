from django.urls import path
#from . import views
from .views import HomeView, ArticleDetailVIew, AddPostView, UpdatePostView

urlpatterns = [
    #path('', views.home, name="home"),
    path('',  HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetailVIew.as_view(), name='article-details'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
]

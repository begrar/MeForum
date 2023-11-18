from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post

#def home(request):
#   return render(request, 'index.html', {})

class HomeView(ListView):
    model = Post
    template_name = 'index.html'


class ArticleDetailVIew(DetailView):
    model = Post
    template_name = 'article_details.html'

class AddPostView(CreateView):
    model = Post
    template_name = 'add_post.html'
    fields = '__all__'
    #fields = ('title', 'body')
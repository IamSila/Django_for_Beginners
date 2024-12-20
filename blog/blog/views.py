from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post



# Create your views here.

#Homepage view
class BlogListView(ListView):
    """This will be used in our homepage"""
    model = Post
    template_name = 'home.html'
    # context_object_name = 

class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
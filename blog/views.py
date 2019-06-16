from django.shortcuts import render
from django.views.generic import ListView, DetailView
# Create your views here.

from .models import Post


class BlogListView(ListView):
    model = Post
    context_object_name = "post_list"


class BlogDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"

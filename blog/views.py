from django.shortcuts import render
from django.views.generic import (
    CreateView, ListView, DetailView, UpdateView, DeleteView
)
from django.urls import reverse_lazy
# Create your views here.

from .models import Post


class BlogCreateView(CreateView):
    model = Post
    template_name = "blog/post_new.html"
    fields = ['title', 'author', 'body']


class BlogListView(ListView):
    model = Post
    context_object_name = "post_list"


class BlogDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"


class BlogUpdateView(UpdateView):
    model = Post
    template_name = "blog/post_edit.html"
    fields = ['title', 'body']


class BlogDeleteView(DeleteView):
    model = Post
    template_name = "blog/post_delete.html"
    success_url = reverse_lazy('blog:post_list')

from django.urls import path

from .views import (
    BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView
)

app_name = 'blog'

urlpatterns = [
    path("new", BlogCreateView.as_view(), name="post_new"),
    path("list", BlogListView.as_view(), name="post_list"),
    path("<int:pk>/detail", BlogDetailView.as_view(), name="post_detail"),
    path("<int:pk>/edit", BlogUpdateView.as_view(), name="post_edit"),
    path("<int:pk>/delete", BlogDeleteView.as_view(), name="post_delete"),
]

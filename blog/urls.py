from django.urls import path

from .views import BlogListView, BlogDetailView

app_name = 'blog'

urlpatterns = [
    path("list", BlogListView.as_view(), name="blog_list"),
    path("post/<int:pk>/", BlogDetailView.as_view(), name="post_detail"),
]

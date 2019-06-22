from django.db import models
from django.urls import reverse

# Create your models here.
# Local


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    body = models.TextField()

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.title[:50]

    def get_absolute_url(self):
        return reverse("blog:post_detail", kwargs={"pk": self.pk})

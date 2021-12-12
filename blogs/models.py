from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from profiles.models import Profile


class BlogPost(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post_title = models.CharField("Post Title", max_length=150, unique=True)
    post_content = models.TextField("Content")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post_title

    class Meta:
        ordering = ("-created",)

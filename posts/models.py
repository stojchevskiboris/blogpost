from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="upload/",default=None, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, editable=True)
    date_modified = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class PostComment(models.Model):
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
    comment = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)


from django.db import models
from django.conf import settings
import os

# Create your models here.
class Post_Sale(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, limit_choices_to={"is_staff": True})
    title = models.CharField(max_length=30)
    contents = models.TextField()
    image = models.ImageField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Post_Sale_Comment(models.Model):
    name = models.ForeignKey(settings.AUTH_USER_MODEL)
    message = models.CharField(max_length=1000)
    post_sale_comment = models.ForeignKey(Post_Sale, related_name='comment_set')
    comment = models.ForeignKey("self", blank=True, null=True, related_name='reply_set')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

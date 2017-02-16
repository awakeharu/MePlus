from django.db import models
from django.conf import settings
import os


class Post_Notice(models.Model):
    manager_name = models.ForeignKey(settings.AUTH_USER_MODEL, limit_choices_to={"admin": True})
    title = models.CharField(max_length=30)
    contents = models.TextField()
    image = models.ImageField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    
class Contact(models.Model):
    name = models.ForeignKey(settings.AUTH_USER_MODEL)
    email = models.EmailField(max_length=70,blank=False)
    massage = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)


class Author(models.Model):
    uploader = models.ForeignKey(settings.AUTH_USER_MODEL, limit_choices_to={"admin": True})
    author = models.CharField(max_length = 20)
    explain = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.author








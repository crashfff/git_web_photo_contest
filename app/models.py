from django.db import models
from django.contrib.auth.models import User


class CustomUser(User):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)


class Like(models.Model):
    author = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
    photo = models.ForeignKey('Photo', on_delete=models.CASCADE)
    like_published = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)



class Photo(models.Model):
    description = models.CharField(max_length=255)
    author = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
    photo_published = models.DateTimeField(auto_now_add=True)
    quantity_comments = models.IntegerField()
    quantity_likes = models.IntegerField()
    is_published = models.BooleanField(default=True)

class Comment(models.Model):
    author = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
    photo = models.ForeignKey('Photo', on_delete=models.CASCADE)
    comment_published = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)


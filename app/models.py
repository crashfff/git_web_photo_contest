from django.db import models
from django.contrib.auth.models import User


class CustomUser(User):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)


class Like(models.Model):
    author = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
    photo = models.ForeignKey('Photo', on_delete=models.CASCADE)
    like_published = models.DateTimeField(null=True)


class Photo(models.Model):
    description = models.CharField(max_length=255)
    author = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
    photo_published = models.DateTimeField(null=True)
    quantity_comments = models.IntegerField()
    quantity_likes = models.IntegerField()


class Comment(models.Model):
    author = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
    photo = models.ForeignKey('Photo', on_delete=models.CASCADE)
    comment_published = models.DateTimeField(null=True)

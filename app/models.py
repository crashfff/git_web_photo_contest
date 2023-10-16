from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class CustomUser(User):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)


class Like(models.Model):
    author = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
    photo = models.ForeignKey('Photo', on_delete=models.CASCADE)
    like_published = models.DateTimeField(auto_now_add=True, null=True)
    is_published = models.BooleanField(default=True)


class Photo(models.Model):
    description = models.CharField(max_length=255)
    author = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
    photo_published = models.DateTimeField(auto_now_add=True, null=True)
    photo_change = models.DateTimeField(auto_now=True)
    quantity_comments = models.IntegerField(default=0)
    quantity_likes = models.IntegerField(default=0)
    is_published = models.BooleanField(default=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", null=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)


    def get_absolute_url(self):
        return reverse('show_photo', kwargs={'photo_id': self.pk})


class Comment(models.Model):
    author = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
    photo = models.ForeignKey('Photo', on_delete=models.CASCADE)
    comment_published = models.DateTimeField(auto_now_add=True, null=True)
    is_published = models.BooleanField(default=True)

class Category(models.Model):
    name = models.CharField(max_length=30, db_index=True)

    def __str__(self):
        return self.name
from django.db import models


class User(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)


class Like(models.Model):
    user = models.ForeignKey('User', on_delete=models.PROTECT, null=True)
    photo = models.ForeignKey('Photo', on_delete=models.PROTECT, null=True)


class Photo(models.Model):
    description = models.CharField(max_length=255)
    author = models.ForeignKey('User', on_delete=models.PROTECT, null=True)


class Comment(models.Model):
    user = models.ForeignKey('User', on_delete=models.PROTECT, null=True)
    photo = models.ForeignKey('Photo', on_delete=models.PROTECT, null=True)

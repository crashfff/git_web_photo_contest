from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.urls import reverse

# создание лайков и комментариев

class CustomUser(AbstractUser):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)

    def get_absolute_url(self):
        return reverse('page_user', kwargs={'user_id': self.pk})


class Like(models.Model):
    author = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
    photo = models.ForeignKey('Photo', on_delete=models.CASCADE)
    like_published = models.DateTimeField(auto_now_add=True, null=True)
    is_published = models.BooleanField(default=True)


class Photo(models.Model):
    title = models.CharField(max_length=255, null=True, verbose_name='Заголовок')
    description = models.CharField(max_length=255, verbose_name='Описание')
    author = models.ForeignKey('CustomUser', on_delete=models.CASCADE,  verbose_name='Автор', null=True)
    photo_published = models.DateTimeField(auto_now_add=True, null=True)
    photo_change = models.DateTimeField(auto_now=True)
    quantity_comments = models.IntegerField(default=0)
    quantity_likes = models.IntegerField(default=0)
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", null=True, verbose_name='Фото')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категории')

    def get_absolute_url(self):
        return reverse('photo', kwargs={'photo_id': self.pk})


class Comment(models.Model):
    author = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
    photo = models.ForeignKey('Photo', on_delete=models.CASCADE)
    comment_published = models.DateTimeField(auto_now_add=True, null=True)
    is_published = models.BooleanField(default=True)

class Category(models.Model):
    name = models.CharField(max_length=30, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})

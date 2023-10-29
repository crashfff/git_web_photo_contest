from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.urls import reverse
from django.dispatch import receiver
from django.db.models.signals import post_save


# создание лайков и комментариев

class CustomUser(AbstractUser):

    def get_absolute_url(self):
        return reverse('page_user', kwargs={'user_id': self.pk})

    class Meta:
        db_table = 'CustomUser_app_db'


class Like(models.Model):
    author = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
    photo = models.ForeignKey('Photo', on_delete=models.CASCADE)
    like_published = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)

    class Meta:
        db_table = 'Like_app_db'


class Photo(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    description = models.CharField(max_length=255, verbose_name='Описание')
    author = models.ForeignKey('CustomUser', on_delete=models.CASCADE, verbose_name='Автор')
    photo_published = models.DateTimeField(auto_now_add=True)
    photo_change = models.DateTimeField(auto_now=True)
    quantity_comments = models.IntegerField(default=0)
    quantity_likes = models.IntegerField(default=0)
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name='Фото')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категории')

    class Meta:
        db_table = 'Photo_app_db'



    def get_absolute_url(self):
        return reverse('photo', kwargs={'photo_id': self.pk})





class Comment(models.Model):
    author = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
    photo = models.ForeignKey('Photo', on_delete=models.CASCADE)
    comment_published = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)

    class Meta:
        db_table = 'Comment_app_db'


class Category(models.Model):
    name = models.CharField(max_length=30, db_index=True)

    class Meta:
        db_table = 'Category_app_db'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})

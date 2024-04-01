from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.contrib.auth.models import AbstractUser
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

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    class Meta:
        db_table = 'Like_app_db'

    def __str__(self):
        return f'Id {self.id}'


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

    user_which_like = models.ManyToManyField('CustomUser', through='Like', related_name='photo_like')

    class Meta:
        db_table = 'Photo_app_db'

    def get_absolute_url(self):
        return reverse('photo', kwargs={'photo_id': self.pk})


class Comment(models.Model):
    author = models.ForeignKey('CustomUser', related_name='comments', on_delete=models.CASCADE)
    photo = models.ForeignKey('Photo', related_name='comments', on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=255, null=True)
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

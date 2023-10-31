from django.db.models import Count
from django.contrib.contenttypes.models import ContentType
from .models import *

menu = [{'title': 'Опубликовать фотографию', 'url_name': 'pub_photo'},]



class DataMixin:
    paginate_by = 3

    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.annotate(Count('photo'))

        user_menu = menu.copy()



        context['menu'] = user_menu

        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context


def add_like(obj, user):
    obj_type = ContentType.objects.get_for_model(obj)
    like, is_created =Like.objects.get_or_create(content_type=obj_type, object_id=obj.id, user=user)
    return like

def remove_like(obj, user):
    """Удаляет лайк с `obj`.
    """
    obj_type = ContentType.objects.get_for_model(obj)
    Like.objects.filter(
        content_type=obj_type, object_id=obj.id, user=user
    ).delete()

def is_fan(obj, user) -> bool:
    """Проверяет, лайкнул ли `user` `obj`.
    """
    if not user.is_authenticated:
        return False
    obj_type = ContentType.objects.get_for_model(obj)
    likes = Like.objects.filter(
        content_type=obj_type, object_id=obj.id, user=user)
    return likes.exists()

def get_fans(obj):
    """Получает всех пользователей, которые лайкнули `obj`.
    """
    obj_type = ContentType.objects.get_for_model(obj)
    return CustomUser.objects.filter(
        likes__content_type=obj_type, likes__object_id=obj.id)
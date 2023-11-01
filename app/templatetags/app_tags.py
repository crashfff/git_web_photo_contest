from django import template
from app.models import *
import random

register = template.Library()


@register.simple_tag(name='getcats')
def get_categories():
    return Category.objects.all()


@register.simple_tag(name='random_number')
def get_random_number():
    #доделать шаблон, если в бд нет постов
    if len(Photo.objects.all()) == 0:
        return ''
    post_list = Photo.objects.filter(is_published=True).values_list('id')
    return str(random.choice(post_list)[0])


@register.inclusion_tag('list_categories.html')
def show_categories():
    cats = Category.objects.all()
    list_of_users = CustomUser.objects.all()
    return {'cats': cats, 'list_of_users': list_of_users}
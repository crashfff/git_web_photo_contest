from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *


menu = ['О сайте', 'Профиль пользователя', 'Список фотографий', 'Список лучших фотографий']


def index(request):
    return render(request, 'index.html', {'menu':menu,'title': 'Главная страница'})


def page_user(request):
    return render(request, 'page_user.html', {'title': 'Страница пользователя'})


def photo(request):
    post = Photo.objects.all()
    return render(request, 'photo.html', {'list_of_photos': post, 'title': 'Фото'})


def list_of_users(request):
    post = CustomUser.objects.all()
    return render(request, 'list_of_users.html', {'list_of_users': post, 'title': 'Главная страница'})

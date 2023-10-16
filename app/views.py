from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *

menu = [{'title': 'О сайте', 'url_name': 'about'},
        {'title':'Опубликовать фотографию','url_name': 'pub_photo'},
        {'title': 'Служба поддержки', 'url_name': 'contact' },
        {'title': 'Войти в профиль', 'url_name': 'login'}]



def index(request):
        post = Photo.objects.all()
        return render(request,
         'index.html',
             {'menu':menu, 'title': 'Главная страница', 'post': post})


def page_user(request):
    context = {'menu': menu,
               'title': 'Страница пользователя'
               }
    return render(request, 'page_user.html', context=context)


def photo(request):
    post = Photo.objects.all()
    context = {'menu': menu,
               'title': 'Страница пользователя'
               }
    return render(request, 'photo.html', {'menu': menu,'list_of_photos': post, 'title': 'Фото'})


def list_of_users(request):
    post = CustomUser.objects.all()
    return render(request, 'list_of_users.html', {'menu': menu, 'list_of_users': post, 'title': 'Список всех пользователей'})

def pub_photo(request):
    return HttpResponse('Опубликование фотографии')

def about(request):
    return HttpResponse('Информация о сайте')

def contact(request):
    return HttpResponse('Служба поддержки')

def login(request):
    return HttpResponse('Авторизация')

def show_photo(request, photo_id):
    return HttpResponse(f'Фотография под id = {photo_id} ')
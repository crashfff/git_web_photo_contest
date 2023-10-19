from django.shortcuts import render, get_object_or_404
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
             {'menu':menu, 'title': 'Главная страница', 'post': post, 'cat_selected': 0})


def page_user(request, user_id):
    list_of_users = CustomUser.objects.all()
    context = {'menu': menu,
                'title': 'Страница пользователя',
                'list_of_users': list_of_users,
                'user_id': user_id,
               }
    return render(request, 'page_user.html', context=context)




def list_of_users(request):
    list_of_users = CustomUser.objects.all()
    return render(request, 'list_of_users.html', {'menu': menu, 'list_of_users': list_of_users, 'title': 'Список всех пользователей'})

def pub_photo(request):
    return HttpResponse('Опубликование фотографии')

def about(request):
    return HttpResponse('Информация о сайте')

def contact(request):
    return HttpResponse('Служба поддержки')

def login(request):
    return HttpResponse('Авторизация')

def show_photo(request, photo_id):
    post = get_object_or_404(Photo, pk=photo_id)
    context = {'menu': menu,
               'title': 'Страница фотографии',
               'post': post,
               'cat_selected': post.cat_id,
               }

    return render(request, 'photo.html', context=context)

def top_photos(request):
    return HttpResponse('Топ фотографий')

def random_photo(request):
    return HttpResponse('Случайная фотография')


def show_category(request, cat_id):

    post = Photo.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()

    return render(request, 'index.html',{'menu':menu, 'title': 'Оторбражение по категориям', 'post': post, 'cats': cats, 'cat_selected': cat_id})

from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from .utils import *
from .form import *
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin
import random




menu = [{'title': 'Опубликовать фотографию', 'url_name': 'pub_photo'},]


class AppIndex(DataMixin, ListView, LoginRequiredMixin):
    model = Photo
    template_name = 'index.html'
    context_object_name = 'post'
    login_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Главная страница")
        kwargs['form'] = AddPostForm

        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Photo.objects.filter(is_published=True)


#
#
# def index(request):
#         post = Photo.objects.all()
#         return render(request,
#          'index.html',
#              {'menu':menu, 'title': 'Главная страница', 'post': post, 'cat_selected': 0})


def page_user(request, user_id):
    post = Photo.objects.all()
    list_of_users = CustomUser.objects.all()
    context = {'menu': menu,
               'title': 'Страница пользователя',
               'list_of_users': list_of_users,
               'user_id': user_id,
               'post': post,
               }
    return render(request, 'page_user.html', context=context)


def list_of_users(request):
    list_of_users = CustomUser.objects.all()
    return render(request, 'list_of_users.html',
                  {'menu': menu, 'list_of_users': list_of_users, 'title': 'Список всех пользователей'})


class Pub_Photo(LoginRequiredMixin, CreateView, AddPostForm):
    form_class = AddPostForm
    login_url = reverse_lazy('login')
    template_name = 'pub_photo.html'
    model = Photo
    success_url = reverse_lazy('pub_photo')

    def get_context_data(self, **kwargs):
        kwargs['form'] = AddPostForm
        kwargs['menu'] = menu
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)
#
# def pub_photo(request):
#     form = AddPostForm(request.POST, request.FILES)
#     if form.is_valid():
#         form = form.save(commit=False)
#         form.save()
#         return redirect('index')
#     else:
#         return render(request, 'pub_photo.html', context={'form': form, 'menu': menu, 'title': 'Добавление фотографии'})


def about(request):
    return HttpResponse('Информация о сайте')


def contact(request):
    return HttpResponse('Служба поддержки')


# def login(request):
#     return HttpResponse('Авторизация')


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


# def random_photo(request):
#     post = Photo.objects.filter(is_published=True).values_list('id')
#     random_id = post[random.randint(0, len(post))][0]
#     # мб сдеать список из всех айди опубликованных фотографий и брать рандомно из этого списка
#     context = {'menu': menu,
#                'title': 'Страница фотографии',
#                'post': post,
#                'random_number': str(random_id),
#                }
#     return render(request, 'random.html', context)



def show_category(request, cat_id):

    post = Photo.objects.filter(cat_id=cat_id, is_published=True)
    cats = Category.objects.all()

    return render(request, 'index.html',{'menu':menu, 'title': 'Оторбражение по категориям', 'post': post, 'cats': cats, 'cat_selected': cat_id})

class RegisterUser(DataMixin, CreateView):

    form_class = RegisterUserForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')

        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')


class LoginUser(DataMixin, LoginView):

    form_class = LoginUserForm
    template_name = 'login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Авторизация')

        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('index')


def logout_user(request):
    logout(request)

    return redirect('index')
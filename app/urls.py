from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('page_user/', views.page_user, name='page_user'),
    path('photo/', views.photo, name='photo'),
]


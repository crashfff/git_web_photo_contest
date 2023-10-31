from django.urls import path
from . import views


urlpatterns = [
    path('', views.AppIndex.as_view(), name='index'),
    path('page_user/<int:user_id>', views.page_user, name='page_user'),
    path('all_users/', views.list_of_users, name='list_of_users'),
    path('pub_photo/', views.Pub_Photo.as_view(), name='pub_photo'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('top_photos/', views.top_photos, name='top_photos'),
    # path('random_photo/', views.random_photo, name='random_photo'),
    path('photo/<int:photo_id>', views.show_photo, name='photo'),
    path('category/<int:cat_id>', views.show_category, name='category'),


]


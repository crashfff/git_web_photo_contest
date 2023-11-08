from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from app.views import *
from website_photo_contest import settings
from rest_framework import routers, serializers, viewsets
from app.models import CustomUser



urlpatterns = [
    path('app/', include('app.urls')),
    path('admin/', admin.site.urls),
    path('api/v1/photos', PhotoList.as_view()),
    path('api/v1/photo/<int:pk>/', PhotoDetail.as_view()),
    path('api/v1/users', CustomUserList.as_view()),
    path('api/v1/user/<int:pk>', CustomUserDetail.as_view()),

]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
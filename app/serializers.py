from rest_framework import serializers
from .models import *


class PhotoSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Photo
        fields = ['id', 'title', 'description', 'photo', 'author', 'cat']


class CustomUserSerializer(serializers.ModelSerializer):
    photos_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'photos_set']

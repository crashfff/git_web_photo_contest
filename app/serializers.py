from rest_framework import serializers
from .models import *


class PhotoSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Photo
        fields = ['id', 'title', 'description', 'photo', 'author', 'cat', 'comments']


class CustomUserSerializer(serializers.ModelSerializer):
    photos_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    categories = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'photos_set', 'comments', 'categories']


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Comment
        fields = ['id', 'comment_text', 'author', 'photo']


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['photo', 'author', 'is_published']

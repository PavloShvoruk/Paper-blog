from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Board, Article, Comment


class UserSerializer(serializers.ModelSerializer):
    """serialization of users"""
    class Meta:
        model = User
        fields = ("id", "username")


class BoardSerializer(serializers.ModelSerializer):
    """Серіалізація категорій(Boards)"""

    class Meta:
        model = Board
        fields = ("__all__")


class ArticleSerializer(serializers.ModelSerializer):
    """Article serialization"""
    author = UserSerializer()
    board = BoardSerializer()
    published_at = serializers.DateTimeField(
        format="%d.%m.%Y, %H:%M:%S", required=False, read_only=True)

    class Meta:
        model = Article
        fields = ("id", "title", "article_text",
                  "published_at", "board", "author")


class CommentSerializer(serializers.ModelSerializer):
    """Comment serialization"""
    created_by = UserSerializer()

    class Meta:
        model = Comment
        fields = ("message", "created_at", "article", "created_by")


class CommentPostSerializer(serializers.ModelSerializer):
    """Comment posting serialization"""
    class Meta:
        model = Comment
        fields = ("message", "article")

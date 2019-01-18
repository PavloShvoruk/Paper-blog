from rest_framework import serializers
from .models import Board, Article


class BoardSerializer(serializers.ModelSerializer):
    """Серіалізація категорій(Boards)"""

    class Meta:
        model = Board
        fields = ("name", "description")


class ArticleSerializer(serializers.ModelSerializer):
    """Article serialization"""
    class Meta:
        model = Article
        fields = ("title", "article_text",
                  "published_at", "board", "author")

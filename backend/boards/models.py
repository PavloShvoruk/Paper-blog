from django.db import models
from django.contrib.auth.models import User
#from djoser.urls.base import User


class Board(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Article(models.Model):
    title = models.CharField(max_length=255)
    article_text = models.CharField(max_length=4000)
    published_at = models.DateTimeField(auto_now_add=True)
    board = models.ForeignKey(
        Board, verbose_name="Category", on_delete=models.CASCADE)
    author = models.ForeignKey(
        User, verbose_name="Article Author", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"


class Comment(models.Model):
    message = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE)
    created_by = models.ForeignKey(
        User, verbose_name="Comment Author", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Article comment"
        verbose_name_plural = "Article comments"

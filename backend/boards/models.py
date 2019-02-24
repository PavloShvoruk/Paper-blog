from django.db import models
from django.contrib.auth.models import User
#from djoser.urls.base import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(
        upload_to='avatars/', max_length=255, null=True, blank=True)


class Board(models.Model):
    name = models.CharField(max_length=30, unique=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=255)
    article_text = models.TextField()
    published_at = models.DateTimeField(auto_now_add=True)
    board = models.ForeignKey(
        Board, verbose_name="Category", on_delete=models.CASCADE)
    author = models.ForeignKey(
        User, verbose_name="Article Author", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"

    def __str__(self):
        return self.title


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

    def __str__(self):
        return self.message

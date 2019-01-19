from django.contrib import admin
from .models import Board, Article, Comment
# Register your models here.


class BoardAdmin(admin.ModelAdmin):
    boards_display = ("name", "description")


class ArticleAdmin(admin.ModelAdmin):
    articles_display = ("title", " article_text",
                        "published_at", "board", "author")


class CommentAdmin(admin.ModelAdmin):
    comments_display = ("message", "created_at", "article", "created_by")


admin.site.register(Board, BoardAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)

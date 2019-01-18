from django.contrib import admin
from .models import Board, Article
# Register your models here.


class BoardAdmin(admin.ModelAdmin):
    boards_display = ("name", "description")


class ArticleAdmin(admin.ModelAdmin):
    articles_display = ("title", " article_text",
                        "published_at", "board", "author")


admin.site.register(Board, BoardAdmin)
admin.site.register(Article, ArticleAdmin)

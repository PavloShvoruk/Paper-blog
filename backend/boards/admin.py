from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Board, Article, Comment, UserProfile
# Register your models here.


class UserInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Users'


class UserAdmin(BaseUserAdmin):
    inlines = (UserInline,)


class BoardAdmin(admin.ModelAdmin):
    boards_display = ("name", "description")


class ArticleAdmin(admin.ModelAdmin):
    articles_display = ("title", " article_text",
                        "published_at", "board", "author")


class CommentAdmin(admin.ModelAdmin):
    comments_display = ("message", "created_at", "article", "created_by")


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Board, BoardAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)

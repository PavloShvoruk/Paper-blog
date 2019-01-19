from django.urls import path
from .views import BoardView, ArticleView, CommentView

urlpatterns = [
    path('categories/', BoardView.as_view()),
    path('articles/', ArticleView.as_view()),
    path('comments/', CommentView.as_view())
]

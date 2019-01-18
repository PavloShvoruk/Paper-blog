from django.urls import path
from .views import BoardView, ArticleView

urlpatterns = [
    path('categories/', BoardView.as_view()),
    path('articles/', ArticleView.as_view())
]

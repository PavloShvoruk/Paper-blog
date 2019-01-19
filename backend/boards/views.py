from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

from .models import Board, Article, Comment
from .serializers import BoardSerializer, ArticleSerializer, CommentSerializer
# Create your views here.


class BoardView(APIView):
    permission_classes = [permissions.AllowAny, ]

    def get(self, request):
        board_set = Board.objects.all()
        board_serializer = BoardSerializer(board_set, many=True)
        return Response({"data": board_serializer.data})


class ArticleView(APIView):

    def get(self, request):
        article_set = Article.objects.all()
        article_serializer = ArticleSerializer(article_set, many=True)
        return Response({"data": article_serializer.data})


class CommentView(APIView):

    def get(self, request):
        comment_set = Comment.objects.all()
        comment_serializer = CommentSerializer(comment_set, many=True)
        return Response({"data": comment_serializer.data})

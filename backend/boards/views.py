from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

from .models import Board, Article, Comment
from .serializers import (
    BoardSerializer, ArticleSerializer, CommentSerializer, CommentPostSerializer)
# Create your views here.


class BoardView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    def get(self, request):
        board_set = Board.objects.all()
        board_serializer = BoardSerializer(board_set, many=True)
        return Response({"data": board_serializer.data})


class ArticleView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    def get(self, request):
        # board = request.GET.get("board")
        # article_set = Article.objects.filter(board=board)
        article_set = Article.objects.all()
        article_serializer = ArticleSerializer(article_set, many=True)
        return Response({"data": article_serializer.data})

    # def post(self, request):


class CommentView(APIView):
    permission_classes = [permissions.IsAuthenticated, ]
    #permission_classes = [permissions.AllowAny, ]

    def get(self, request):
        article = request.GET.get("article")
        comment_set = Comment.objects.filter(article=article)
        comment_serializer = CommentSerializer(comment_set, many=True)
        return Response({"data": comment_serializer.data})

    def post(self, request):
        comment = CommentPostSerializer(data=request.data)
        if comment.is_valid():
            comment.save(created_by=request.user)
            return Response({"status": "Add comment"})
        else:
            return Response({"status": "Error"})

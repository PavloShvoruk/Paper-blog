from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

from .models import Board, Article
from .serializers import BoardSerializer, ArticleSerializer
# Create your views here.


class BoardView(APIView):

    def get(self, request):
        board_set = Board.objects.all()
        board_serializer = BoardSerializer(board_set, many=True)
        return Response(board_serializer.data)


class ArticleView(APIView):

    def get(self, request):
        article_set = Article.objects.all()
        article_serializer = ArticleSerializer(article_set, many=True)
        return Response(article_serializer.data)

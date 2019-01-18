from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

from .models import Board
from .serializers import BoardSerializer
# Create your views here.


class BoardView(APIView):

    def get(self, request):
        board = Board.objects.all()

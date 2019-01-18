from rest_framework import serializers
from .models import Board


class BoardSerializer(serializers.ModelSerializer):
    """Серіалізація категорій(Boards)"""

    class Meta:
        model = Board
        fields = ("name", "description")

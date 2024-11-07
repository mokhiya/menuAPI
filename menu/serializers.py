from rest_framework import serializers
from .models import MenuModel, CommentModel


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuModel
        fields = ['id', 'title', 'description', 'price', 'created_at']


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = CommentModel
        fields = ['id', 'user', 'meal', 'comment', 'created_at']

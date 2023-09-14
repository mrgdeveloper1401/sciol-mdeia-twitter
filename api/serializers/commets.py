from rest_framework import serializers
from post.models import CommentModel


class CommentsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentModel
        fields = '__all__'
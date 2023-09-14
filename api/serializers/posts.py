from rest_framework import serializers
from post.models import PostModel


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostModel
        fields = '__all__'
        
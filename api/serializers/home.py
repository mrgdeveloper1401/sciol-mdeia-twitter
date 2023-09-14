from rest_framework import serializers
from post.models import PostModel


class HomeSerializers(serializers.ModelSerializer):
    class Meta:
        model = PostModel
        fields = ('user', 'body', 'location')
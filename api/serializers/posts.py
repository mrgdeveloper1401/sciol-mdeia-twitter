from rest_framework import serializers
from post.models import PostModel
from api.serializers.commets import CommentsCreateSerializer


class PostCreateSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()
    class Meta:
        model = PostModel
        fields = '__all__'
        
    def get_comments(self, obj):
        result = obj.pcomment.all()
        return CommentsCreateSerializer(instance=result, many=True).data
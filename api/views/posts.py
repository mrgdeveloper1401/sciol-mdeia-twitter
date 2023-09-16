from rest_framework.views import APIView
from api.serializers.posts import PostCreateSerializer
from post.models import PostModel
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


class PostGetApiView(APIView):
    def get(self, request):
        post = PostModel.objects.all()
        ser_data = PostCreateSerializer(instance=post, many=True)
        return Response(ser_data.data, status=status.HTTP_200_OK)
        
        
class PostCreateApiView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def post(self, request):
        ser_data = PostCreateSerializer(data=request.data)
        if ser_data.is_valid():
            ser_data.save()
            return Response(ser_data.data, status=status.HTTP_201_CREATED)
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)
        

class PostUpdateApiView(APIView):
    permission_classes = (IsAuthenticated, )
    def put(self, request, post_id):
        post = PostModel.objects.get(pk=post_id)
        ser_data = PostCreateSerializer(instance=post, data=request.data, partial=True)
        if ser_data.is_valid():
            ser_data.save()
            return Response(ser_data.data, status=status.HTTP_201_CREATED)
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)

class PostDeleteApiview(APIView):
    permission_classes = (IsAuthenticated, )
    
    def delete(self, request, post_id):
        post = PostModel.objects.get(pk=post_id)
        post.delete()
        return Response({'message': 'successfly delete post'}, status=status.HTTP_204_NO_CONTENT)

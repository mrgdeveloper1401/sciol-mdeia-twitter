from rest_framework.views import APIView
from api.serializers.posts import PostCreateSerializer
from post.models import PostModel
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

class PostCreateApiView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def post(self, request):
        ser_data = PostCreateSerializer(data=request.data)
        if ser_data.is_valid():
            ser_data.save()
            return Response(ser_data.data, status=status.HTTP_201_CREATED)
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)
        

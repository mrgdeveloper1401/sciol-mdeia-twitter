from rest_framework.views import APIView
from rest_framework.response import Response
from api.serializers.commets import CommentsCreateSerializer
from rest_framework import status
from post.models import CommentModel


class CommetsGetApiView(APIView):
    def get(self, request):
        comment = CommentModel.objects.all()
        ser_data = CommentsCreateSerializer(instance=comment, many=True)
        return Response(ser_data.data, status=status.HTTP_200_OK)
        
        
class CommentsCreateApiView(APIView):
    def post(self, request):
        ser_data = CommentsCreateSerializer(data=request.data, many=True)
        if ser_data.is_valid():
            ser_data.save()
            return Response(ser_data.data, status=status.HTTP_201_CREATED)
        return Response(ser_data.errors, status=status.HTTP_201_CREATED)
        
        
class CommetsUpdateApiView(APIView):
    def put(self, request):
        ...
        
class CommetsDeleteApiView(APIView):
    def delete(self, request):
        ...
        
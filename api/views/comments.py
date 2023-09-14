from rest_framework.views import APIView
from rest_framework.response import Response
from api.serializers.commets import CommentsCreateSerializer
from rest_framework import status


class CommentsCreateApiView(APIView):
    def post(self, request):
        ser_data = CommentsCreateSerializer(data=request.data)
        if ser_data.is_valid():
            ser_data.save()
            return Response(ser_data.data, status=status.HTTP_201_CREATED)
        return Response(ser_data.errors, status=status.HTTP_201_CREATED)
        
        
        
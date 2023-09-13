from rest_framework.views import APIView
from serializers.posts import PostCreateSerializer


class PostCreateApiView(APIView):
    def post(self, request):
        ser_data = PostCreateSerializer(data=request.data)
        

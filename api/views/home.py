from rest_framework.views import APIView
from api.serializers.home import HomeSerializers
from rest_framework.response import Response
from post.models import PostModel


class HomeView(APIView):
    def get(self, request):
        post = PostModel.objects.all()
        ser_data = HomeSerializers(instance=post, many=True)
        return Response(data=ser_data.data)
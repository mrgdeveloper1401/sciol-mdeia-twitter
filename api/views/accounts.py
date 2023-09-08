from rest_framework.response import Response
from api.serializers.account import SignupSerializers
from rest_framework.views import APIView
from accounts.models import User


class SignUpApiView(APIView):
    def post(self, request):
        ser_data = SignupSerializers(data=request.data)
        if ser_data.is_valid():
            User.objects.create_user(
                full_name = ser_data._validated_data['full_name'],
                username = ser_data._validated_data['username'],
                email = ser_data._validated_data['email'],
                mobile_phone = ser_data.validated_data['mobile_phone'],
                password= ser_data.validated_data['password'],
                
                
            )
            return Response(ser_data.data)
        return Response(ser_data.errors)
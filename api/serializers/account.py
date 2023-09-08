from rest_framework import serializers
from accounts.models import User


class SignupSerializers(serializers.ModelSerializer):
    password2 = serializers.CharField(required=True, wite_only=True)
    class Meta:
        model = User
        fields = ('full_name', 'username', 'email', 'mobile_phone', 'password', 'password2')
        


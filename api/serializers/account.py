from rest_framework import serializers
from accounts.models import User


class SignupSerializers(serializers.ModelSerializer):
    # password2 = serializers.CharField(required=True)
    class Meta:
        model = User
        fields = ('full_name', 'username', 'email', 'mobile_phone', 'password')
        extra_kwargs = {
            'password': {'write_only': True},
            
        }
        
    def validate_username(self, value):
        if value in 'admin':
            raise serializers.ValidationError('username dont be admin')
        elif value in 'root':
            raise serializers.ValidationError('username dont be root')
        return value
    
    # def validate(self, data):
    #     if data['password'] != data['password2']:
    #         raise serializers.ValidationError('password must mach')
    #     return data
    
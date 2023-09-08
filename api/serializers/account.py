from rest_framework import serializers
from accounts.models import User


class SignupSerializers(serializers.ModelSerializer):
    password2 = serializers.CharField(required=True)
    class Meta:
        model = User
        fields = ('full_name', 'username', 'email', 'mobile_phone', 'password')
        extra_kwargs = {'password': {'write_only': True},}
        
    def create(self, validated_data):
        del validated_data['password2']
        return User.objects.create_user(**validated_data)

    def validate_username(self, value):
        if value == 'admin' or value == 'root':
            return serializers.ValidationError('admin or root cant be username')
        return value
    
    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError('password must mach')
        return data
    
    def validate_email(self, value):
        if 'admin' == value or 'root' == value:
            raise serializers.ValidationError('admin or root cant be email')
        return value
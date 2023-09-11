from rest_framework import serializers
from accounts.models import User, RelationUserModel


class SignupSerializers(serializers.ModelSerializer):
    password2 = serializers.CharField(required=True, write_only=True)
    class Meta:
        model = User
        fields = ('full_name', 'username', 'email', 'mobile_phone', 'password', 'password2')
        extra_kwargs = {
            'password': {'write_only': True},
            
        }
        
    def validate_username(self, value):
        if value in 'admin':
            raise serializers.ValidationError('username dont be admin')
        elif value in 'root':
            raise serializers.ValidationError('username dont be root')
        return value
    
    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError('password must be same')
        return data
    
    def create(self, validated_data):
        return super().create(validated_data)
class RelationserializerUser(serializers.ModelSerializer):
    class Meta:
        model = RelationUserModel
        fields = ('from_user', 'to_user',)

    
    
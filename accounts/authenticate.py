from typing import Optional
from django.contrib.auth.backends import BaseBackend, ModelBackend
from django.contrib.auth.base_user import AbstractBaseUser
from .models import User


class UsernameBaeckEnd(BaseBackend):
    def authenticate(self,request, username=None, password=None):
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
            return None
        except User.DoesNotExist:
            return None
            
    def get_user(self, user_id):
        try:
            User.objects.get(pk=user_id)
        
        except User.DoesNotExist:
            return None
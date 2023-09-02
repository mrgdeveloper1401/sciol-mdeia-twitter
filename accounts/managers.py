from django.contrib.auth.models import BaseUserManager, UserManager
from django.contrib.auth.hashers import make_password


class MyManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Please provide an email address')
        
        email = self.normalize_email(email)
        
        user = self.model(
            email=email,
            
        )
        user.password = make_password(password)
        user.save(using=self._db)
        return user
        
    def create_superuser(self, email, username, full_name, mobile_phone , password=None):
        if not username:
            raise ValueError('username must be set')
        if not full_name:
            raise ValueError('full_name must be set')
        if not mobile_phone:
            raise ValueError('mobile_phone must be set')
        
        user = self.create_user(
            email=email,
            password=password
        )
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
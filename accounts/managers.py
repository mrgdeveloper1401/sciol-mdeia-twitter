from django.contrib.auth.models import BaseUserManager, UserManager
from django.contrib.auth.hashers import make_password


class MyManager(BaseUserManager):
    def create_user(self, email,username, full_name,mobile_phone, password=None):
        if not email:
            raise ValueError('Please provide an email address')
        if not username:
            raise ValueError('Please provide an username')
        if not full_name:
            raise ValueError('Please provide an email address')
        email = self.normalize_email(email)
        if not mobile_phone:
            raise ValueError('Please provide a mobile phone')
        
        user = self.model(
            email=email,
            username=username,
            full_name=full_name,
            mobile_phone=mobile_phone,
            
            
            
            
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
        
    def create_superuser(self, email, username, full_name, mobile_phone , password=None):
        
        user = self.create_user(
            email=email,
            password=password,
            username=username,
            full_name=full_name,
            mobile_phone=mobile_phone,
            
            
        )
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
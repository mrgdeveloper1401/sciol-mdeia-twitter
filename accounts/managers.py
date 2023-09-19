from django.contrib.auth.models import BaseUserManager, UserManager
from django.contrib.auth.hashers import make_password


class MyManager(BaseUserManager):
    def create_user(self, email, full_name, password=None):
        if not email:
            raise ValueError('Please provide an email address')
        email = self.normalize_email(email)
        if not full_name:
            raise ValueError('Please provide an email address')
        
        user = self.model(
            email=email,
            full_name=full_name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
        
    def create_superuser(self, email ,full_name, password=None):
        
        user = self.create_user(
            email=email,
            password=password,
            full_name=full_name,
        )
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
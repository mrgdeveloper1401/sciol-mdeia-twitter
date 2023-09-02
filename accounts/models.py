from django.urls import reverse
from django.utils import timezone
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from .managers import MyManager


class User(AbstractBaseUser):
    username = models.CharField(_("Username"), max_length=100, unique=True)
    email = models.EmailField(_("Email"), max_length=255, unique=True)
    full_name = models.CharField(_("Full name"), max_length=255)
    mobile_phone = models.BooleanField(_("Mobile"), max_length=11, unique=True)
    birthday = models.DateField(_("Birthday"), auto_now=timezone.now())
    profile_image = models.ImageField(_("Profile"), upload_to = 'images/profile')
    banner_image = models.ImageField(_("Profile"), upload_to = 'images/banner_profile')
    is_admin = models.BooleanField(_("is admin"), default=False)
    is_active = models.BooleanField(_("is active"), default=True)
    is_superuser = models.BooleanField(_("is superuser"), default=False)
    
    gender = (
        ('male', 'male'),
        ('female', 'female'),
    )
    gender_choose = models.CharField(_("Gender"), max_length=6, choices=gender)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["email", 'mobile_phone', 'full_name']
    
    objects = MyManager()
    def has_perm(self, perm, obj=None):
        return True
    
    def has_mudle_perm(self, app_labe):
        return True
    
    def __str__(self) :
        return self.username
    
    def get_absolute_url(self):
        return reverse("model_detail", kwargs={"pk": self.pk})
    
    
    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")
        db_table = "users-model"
from django.urls import reverse
from django.utils import timezone
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from .managers import MyManager
from core.models import CreateModel, UpdateModel


class User(AbstractBaseUser, CreateModel, UpdateModel):
    username = models.CharField(_("Username"), max_length=100, unique=True)
    email = models.EmailField(_("Email"), max_length=255, unique=True)
    full_name = models.CharField(_("Full name"), max_length=255)
    mobile_phone = models.CharField(_("Mobile"), max_length=11, unique=True)
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
    REQUIRED_FIELDS = ['mobile_phone', 'full_name', 'username']
    
    objects = MyManager()
    
    def has_perm(self, perm, obj=None):
        if self.is_active and self.is_superuser:
            return True
    
    def has_module_perms(self, app_labe):
        if self.is_active and self.is_superuser:
            return True
        
    def get_absolute_url(self):
        return reverse('accounts:profile', args=(self.id))
    
    @property
    def is_staff(self):
        return self.is_admin
    
    def __str__(self) :
        return self.username
    
    def get_absolute_url(self):
        return reverse("model_detail", kwargs={"pk": self.pk})
    
    
    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")
        db_table = "users-model"
        

class RelationUserModel(CreateModel):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    
    class Meta:
        verbose_name = _('relation')
        verbose_name_plural = _('relations')
        db_table = 'relation-model'
    def __str__(self) -> str:
        return f'{self.from_user}  {self.to_user}'
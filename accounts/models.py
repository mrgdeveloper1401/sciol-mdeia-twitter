from django.urls import reverse
from django.utils import  timezone
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from .managers import MyManager
from core.models import CreateModel, UpdateModel, DeleteModel


class User(AbstractBaseUser, CreateModel, UpdateModel):
    username = models.CharField(_("Username"), max_length=100, unique=True)
    email = models.EmailField(_("Email"), max_length=255, unique=True)
    full_name = models.CharField(_("Full name"), max_length=255)
    mobile_phone = models.CharField(_("Mobile"), max_length=11, unique=True)
    birthday = models.DateField(_("Birth day"), default=timezone.now)
    is_admin = models.BooleanField(_("is admin"), default=False)
    is_active = models.BooleanField(_("is active"), default=True)
    is_superuser = models.BooleanField(_("is superuser"), default=False)
    
    gender = (
        ('1', 'male'),
        ('2', 'female'),
    )
    gender_choose = models.CharField(_("Gender"), max_length=1, choices=gender)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['mobile_phone', 'full_name', 'username']
    
    objects = MyManager()
    
    def has_perm(self, perm, obj=None):
        # if self.is_active and self.is_superuser:
            return True
    
    def has_module_perms(self, app_labe):
        # if self.is_active and self.is_superuser:
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
    
    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()
    
    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")
        db_table = "users-model"
        
        
class Imageuser(CreateModel):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    image = models.ImageField(upload_to='profile')
    
    class Meta:
        verbose_name = _('image user')
        verbose_name_plural = _('image users')
        db_table = 'image_user_model'
        
class RecycleUser(User):
    deleted = MyManager()
    class Meta:
        proxy = True


class RelationUserModel(CreateModel):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    
    class Meta:
        verbose_name = _('relation')
        verbose_name_plural = _('relations')
        db_table = 'relation-model'
    def __str__(self) -> str:
        return f'{self.from_user}  {self.to_user}'


class NotificationModel(CreateModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Unotification')
    body = models.TextField(_('body notification'))
    
    class Meta:
        verbose_name = _('notification-model')
        verbose_name_plural = _('notifications-models')
        db_table = 'notofication-model'
        

class OtpCode(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    mobile_phone = models.CharField(_('mobile'), max_length=11, unique=True, blank=True)
    active_code = models.PositiveIntegerField()
    
    def __str__(self):
        return f'{self.email} -- {self.mobile_phone}'
    
    class Meta:
        verbose_name = _('otp-code')
        verbose_name_plural = _('otp-codes')
        db_table = 'otp-code-model'
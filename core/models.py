from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


class CreateModel(models.Model):
    create_at = models.DateTimeField(_('create_at'), auto_now=True)
    
    class Meta:
        verbose_name = _('create_model')
        verbose_name_plural = _('create_models')
        abstract = True


class UpdateModel(models.Model):
    update_at = models.DateTimeField(_('update_at'), auto_now_add=True)
    
    class Meta:
        verbose_name = _('update_model')
        verbose_name_plural = _('update_models')
        abstract = True
        
        
class DeleteModel(models.Model):
    deleted_at = models.DateTimeField(_('deleted_at'), auto_now_add=True)
    is_deleted = models.BooleanField(_('is_deleted'), default=False, editable=False)

    class Meta:
        verbose_name = _('delete_model')
        verbose_name_plural = _('delete_models')
        abstract = True
        
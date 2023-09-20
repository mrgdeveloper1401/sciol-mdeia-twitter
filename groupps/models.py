from django.db import models
from django.utils.translation import gettext_lazy as _
from accounts.models import User
from core.models import CreateModel, UpdateModel


class groupss(CreateModel):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='Ugroups')
    add_user = models.ManyToManyField(User)
    body = models.TextField(_('text'))
    
    class Meta:
        verbose_name = 'group'
        verbose_name_plural = 'groups'
        db_table = 'groups-model'

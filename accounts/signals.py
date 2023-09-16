from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import User, NotificationModel


def create_notification(sender, **kwargs):
    if kwargs['created']:
        NotificationModel.objects.create
    
post_save.connect(receiver=create_notification, sender=User)
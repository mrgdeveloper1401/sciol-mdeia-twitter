from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import User, NotificationModel


@receiver(signal=post_save, sender=User)
def create_user_notification(sender, instance, created, **kwargs):
    if created:
        NotificationModel.objects.create(
            user=instance,
            body='successfly create account'
        )
        
@receiver(signal=post_save, sender=User)
def update_profile_notification(sender, instance, created, **kwargs):
    if  not created:
        NotificationModel.objects.create(
            user=instance,
            body='successfly update accounts'
        )
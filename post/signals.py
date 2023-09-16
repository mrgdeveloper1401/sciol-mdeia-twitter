from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from .models import PostModel
from accounts.models import NotificationModel

@receiver(signal=post_save, sender=PostModel)
def create_post_notification(sender, instance, created, **kwargs):
    if created:
        NotificationModel.objects.create(
            user = instance.user,
            body='create post succsfly'
        )
        

@receiver(signal=post_delete, sender=PostModel)
def delete_post_notification(sender, instance, **kwargs):
        NotificationModel.objects.create(
            user=instance.user,
            body='delete post successfly'
        )
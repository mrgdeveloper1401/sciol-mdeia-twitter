from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from core.models import *
from accounts.models import User


class PostModel(CreateModel, UpdateModel, DeleteModel):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='post_users')
    body = models.TextField(help_text='Please write caption')
    image = models.ImageField(upload_to='posts',blank=True, null=True, help_text='Please upload your image')
    video = models.FileField(upload_to='post/video', blank=True, null=True, help_text='please upload your video')
    location = models.CharField(max_length=730, blank=True, null=True,
                                help_text='You can write the location of this post')
    slug = models.SlugField()
    class StatusPost(models.Model):
        class StatusPosts(models.TextChoices):
            Published = 'pb', 'published'
            Rejected = 'rg', 'rejected'

        choose_status = models.CharField(
            max_length=2,
            choices=StatusPosts.choices,
            default=StatusPosts.Published
        )



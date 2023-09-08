from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from core.models import *
from accounts.models import User
from django.urls import reverse


class PostModel(CreateModel, UpdateModel):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='post_users')
    body = models.TextField(help_text='Please write caption')
    image = models.ImageField(upload_to='posts',blank=True, null=True, help_text='Please upload your image')
    video = models.FileField(upload_to='post/video', blank=True, null=True, help_text='please upload your video')
    location = models.CharField(max_length=730, blank=True, null=True,
                                help_text='You can write the location of this post')
    slug = models.SlugField(max_length=30)
    
    def __str__(self):
        return f'{self.user} -- {self.slug}'
    
    
    def get_absolute_url(self):
        return reverse("post:post_details", args=(self.id, self.slug))
    
    class StatusPost(models.Model):
        class StatusPosts(models.TextChoices):
            Published = 'pb', 'published'
            Rejected = 'rg', 'rejected'

        choose_status = models.CharField(
            max_length=2,
            choices=StatusPosts.choices,
            default=StatusPosts.Published
        ) 
    
    class Meta:
        verbose_name = _('post')
        verbose_name_plural = _('posts')
        db_table = 'post-model'
        
        # order in database and show web
        ordering = ('-create_at', 'body', )
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from core.models import *
from accounts.models import User
from django.urls import reverse


class PostModel(CreateModel, UpdateModel):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='posts')
    body = models.TextField(max_length=500)
    image = models.ImageField(upload_to='posts',blank=True, null=True, help_text='Please upload your image')
    video = models.FileField(upload_to='post/video', blank=True, null=True, help_text='please upload your video')
    location = models.CharField(max_length=730, blank=True, null=True,
                                help_text='You can write the location of this post')
    slug = models.SlugField(max_length=30)
    
    def __str__(self):
        return f'{self.user} -- {self.body}'
    
    
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
        

class CommentModel(CreateModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ucomment')
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE, related_name='pcomment')
    body = models.TextField(max_length=400)
    is_reply = models.BooleanField(default=False)
    reply = models.ForeignKey('self', on_delete=models.CASCADE, related_name='rcomment', blank=True, null=True)
    
    class Meta:
        verbose_name = _('comment')
        verbose_name_plural = _('comments')
        db_table = 'comment-model'
        ordering = ('-create_at', 'body', )
        
    def __str__(self) -> str:
        return f'{self.user} {self.body[:30]}'
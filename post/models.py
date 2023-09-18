from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from core.models import *
from accounts.models import User
from django.urls import reverse
from django.utils.text import slugify


class PostModel(CreateModel, UpdateModel):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='posts')
    body = models.TextField(max_length=500)
    slug = models.SlugField()
    is_active = models.BooleanField(default=True)
    post_tag = models.ManyToManyField('TagPostModel', blank=True, related_name='Ptag')
    

    
    def __str__(self):
        return f'{self.user} -- {self.body}[:30]'
    
    
    def get_absolute_url(self):
        return reverse("post:post_details", args=(self.id, self.slug))

    
    class Meta:
        verbose_name = _('post')
        verbose_name_plural = _('posts')
        db_table = 'post-model'
        
        # order in database and show web
        ordering = ('-create_at', 'body', )
        

class PostOptionModel(models.Model):
    post = models.OneToOneField(PostModel, on_delete=models.PROTECT)
    image = models.FileField(upload_to='post/image', null=True, blank=True)
    video = models.FileField(upload_to='post/video', null=True, blank=True)

    def __str__(self) -> str:
        return str(self.post)[:30]
    
    class Meta:
        verbose_name = _('PostOptionModel')
        verbose_name_plural = _('PostOptionModels')
        db_table = 'post-option-models'
        
        
class RecyclePost(PostModel):
    class Meta:
        proxy = True


class CommentModel(CreateModel, UpdateModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ucomment')
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE, related_name='pcomment')
    body = models.TextField(max_length=400)
    reply = models.ForeignKey('self', on_delete=models.CASCADE, related_name='rcomment', blank=True, null=True)
    is_reply = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = _('comment')
        verbose_name_plural = _('comments')
        db_table = 'comment-model'
        ordering = ('-create_at', 'body', )
        
    def __str__(self) -> str:
        return f'{self.user} - {self.body[:30]}'
    
    
class CommentsOptionModel(models.Model):
    comment = models.OneToOneField(PostModel, on_delete=models.PROTECT)
    image = models.FileField(upload_to='post/image', null=True, blank=True)
    video = models.FileField(upload_to='post/video', null=True, blank=True)
    
    def __str__(self) -> str:
        return str(self.comment)[:30]
    
    class Meta:
        verbose_name = 'CommentOption'
        verbose_name_plural = 'CommentOptions'
        db_table = 'comment-option-model'
        
    
class RecycleComment(CommentModel):
    class Meta:
        proxy = True
        

class RelationPostModel(CreateModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Urelation')
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE, related_name='Prelation')
    like = models.BooleanField(default=None)
    
    # def get_like(self):
    #     return self.like.count()
    
    class Meta:
        verbose_name = _('relation post')
        verbose_name_plural = _('relation posts')
        db_table = 'Relation-post-model'
        


class TagPostModel(models.Model):
    title = models.CharField(max_length=50)
    
    
    def __str__(self) -> str:
        return self.title
    class Meta:
        verbose_name = 'tag post'
        verbose_name_plural = 'tag posts'
        db_table = 'tag-post-model'
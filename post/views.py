from typing import Any
from django import http
from django.shortcuts import render, redirect
from django.views import View
from .models import PostModel
from accounts.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .forms import PostUpdateForm
from django.utils.text import slugify


class HomeView(View):
    template_name = 'post/home.html'
    
    def get(self, request):
        post = PostModel.objects.all()
        return render(request, self.template_name, {'post': post})
    

class PostDetailsView(LoginRequiredMixin, View):
    
    def setup(self, request, *args, **kwargs):
        self.post = PostModel.objects.get(pk=kwargs['post_id'], slug=kwargs['post_slug'])
        return super().setup(request, *args, **kwargs)
    
    template_name = 'post/post_details.html'
    
    def get(self, request, *args, **kwargs):
        post = self.post
        context = {
            'post': post,
            }
        return render(request, self.template_name, context)
    

class PostDeleteView(LoginRequiredMixin, View):
    
    def setup(self, request, *args, **kwargs):
        self.post = PostModel.objects.get(pk=kwargs['post_id'])
        return super().setup(request, *args, **kwargs)
    
    
    def get(self, request, *args, **kwargs):
        post = self.post
        context = {
            'post': post
        }
        if request.user.id == post.user.id:
            post.delete()
            messages.success(request, 'Delete post', 'success')
            return redirect('post:home')
        else:
            messages.error(request, 'Dont delete post', 'warning')
            
        return render(request, '', context)
    
class UpdatePostView(LoginRequiredMixin, View):
    
    def setup(self, request, *args, **kwargs):
        self.post_instance = PostModel.objects.get(pk=kwargs['post_id'])
        return super().setup(request, *args, **kwargs)
    
    def dispatch(self, request, *args, **kwargs):
        post = self.post_instance
        if not post.user.id == request.user.id:
            messages.error(request, 'Invalid', 'warning')
            return redirect('post:home')
        return super().dispatch(request, *args, **kwargs)
    
    
    from_class = PostUpdateForm
    template_name = 'post/update.html'
    
    def get(self, request, *args, **kwargs):
        post = self.post_instance
        update = self.from_class(instance=post)
        return render(request, self.template_name, {'update': update})
    
    def post(self, request, *args, **kwargs):
        post = self.post_instance
        update = self.from_class(request.POST, instance=post)
        if update.is_valid():
            new_save = update.save(commit=False)
            new_save.slug = slugify(update.cleaned_data['body'][:30])
            new_save.save()
            messages.success(request, 'Update Success', 'success')
            return redirect('post:post_details', post.id, post.slug)
        return render(request, self.template_name, {'update': update})
    
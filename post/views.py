from django.shortcuts import render, redirect
from django.views import View
from .models import PostModel
from accounts.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages


class HomeView(View):
    template_name = 'post/home.html'
    
    def get(self, request):
        post = PostModel.objects.all()
        return render(request, self.template_name, {'post': post})
    

class PostDetailsView(LoginRequiredMixin, View):
    template_name = 'post/post_details.html'
    
    def get(self, request, *args, **kwargs):
        post = PostModel.objects.get(pk=kwargs['post_id'], slug=kwargs['post_slug'])
        # user = User.objects.all(user=post)
        context = {
            'post': post,
            # 'user': user,
            
            
        }
        return render(request, self.template_name, context)
    

class PostDeleteView(LoginRequiredMixin, View):
    def get(self, request, post_id):
        post = PostModel.objects.get(pk=post_id)
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
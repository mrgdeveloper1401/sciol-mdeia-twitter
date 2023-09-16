from typing import Any
from django import http
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.views import View
from .models import PostModel, CommentModel, RelationPostModel
from accounts.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .forms import PostCreateUpdateForm, CommentForm, PostSearchForms
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class HomeView(View):
    template_name = 'post/home.html'
    from_class = PostSearchForms
    
    def get(self, request):
        post = PostModel.objects.all()
        if request.GET.get('search'):
            post = post.filter(body__contains=request.GET['search'])
            
        context = {
            'post': post,
            # 'comments': comments
            'search': self.from_class,
            
        }
        return render(request, self.template_name, context)
    

class PostDetailsView(LoginRequiredMixin, View):

    
    def setup(self, request, *args, **kwargs):
        self.post_instance = get_object_or_404(PostModel, pk=kwargs['post_id'], slug=kwargs['post_slug'])
        return super().setup(request, *args, **kwargs)
    
    template_name = 'post/post_details.html'
    form_class = CommentForm
    
    def get(self, request, *args, **kwargs):
        post_user = self.post_instance
        comment = post_user.pcomment.all()
        
        context = {
            'post_user': post_user,
            'comment': comment
            
        }
        return render(request, self.template_name, context)
        
    def post(self, request, *args, **kwargs):
        pass


class PostDeleteView(LoginRequiredMixin, View):
    
    def setup(self, request, *args, **kwargs):
        self.post = get_object_or_404(PostModel, pk=kwargs['post_id'])
        # self.post = PostModel.objects.get(pk=kwargs['post_id'])
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
        self.post_instance = get_object_or_404(PostModel, pk=kwargs['post_id'])
        return super().setup(request, *args, **kwargs)
    
    def dispatch(self, request, *args, **kwargs):
        post = self.post_instance
        if not post.user.id == request.user.id:
            messages.error(request, 'Invalid', 'warning')
            return redirect('post:home')
        return super().dispatch(request, *args, **kwargs)
    
    
    from_class = PostCreateUpdateForm
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

    
class PostCreateView(LoginRequiredMixin, View):
    
    def setup(self, request, *args, **kwargs):
        self.user = get_object_or_404(User, pk=kwargs['user_id'])
        # self.user = User.objects.get(pk=kwargs['user_id'])
        return super().setup(request, *args, **kwargs)
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.id != self.user.id:
            messages.error(request, 'invalid user', 'warning')
            return redirect('post:home')
        return super().dispatch(request, *args, **kwargs)
    
    
    
    form_class = PostCreateUpdateForm
    template_name = 'post/create_post.html'
    
    def get(self, request, *args, **kwargs):
        create_post = self.form_class()
        return render(request, self.template_name, {'create': create_post})
    
    def post(self, request, *args, **kwargs):
        create = self.form_class(request.POST)
        if create.is_valid():
            cd = create.cleaned_data
            new_create = create.save(commit=False)
            new_create.user = request.user
            new_create.slug = slugify(cd['body'][:30])
            new_create.save()
            messages.success(request, 'create post', 'success')
            return redirect('post:home')
        return render(request, self.template_name, {'create': create})
    

# class CommentView(View):
#     def get(self, request):
#         comment = CommentModel.objects.filter(is_reply=True)
#         return render(request, )


class RelationPostLikeView(View):
    def get(self, reqeust, *args, **kwargs):
        post = get_object_or_404(PostModel, pk=kwargs['post_id'])
        like = RelationPostModel.objects.filter(post=post, user=reqeust.user)
        if like.exists():
            messages.error(reqeust, 'you liked post', 'danger')
            
        RelationPostModel.objects.create(post=post, user=reqeust.user)
        messages.success(reqeust, 'post like', 'success')
class RelationPostDislikeView(View):
    def get(self, reqeust, *args, **kwargs):
        ...
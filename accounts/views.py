from typing import Any
from django import http
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from .models import User, RelationUserModel, NotificationModel
from .form import UserCreationForms, UserChangeForms, UserSignIn, UserSignUpForm, UserEditProfileForm
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm 
from django.contrib.auth.mixins import LoginRequiredMixin
from post.models import PostModel
from django.contrib.auth import views as auth_views
from django.urls import reverse, reverse_lazy


class UserSignupView(View):
    form_class = UserSignUpForm
    template_name = 'accounts/singup.html'
    
    def get(self, reques):
        form = self.form_class()
        return render(reques, self.template_name, {'form': form})
    
    def post(self,requests):
        form = self.form_class(requests.POST)
        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create_user(
                mobile_phone=cd['mobile_phone'], 
                username=cd['username'],
                email=cd['email'],
                full_name = cd['full_name'],
                password=cd['password'],
                
            )
            messages.success(requests, 'successfully create account', 'success')
            return redirect('post:home')
        return render(requests, self.template_name, {'form': form})


class SignInView(View):

    def setup(self, request, *args, **kwargs):
        self.next = request.GET.get('next', None)
        return super().setup(request, *args, **kwargs)
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('post:home')
        return super().dispatch(request, *args, **kwargs)
    
    form_class = UserSignIn
    template_name = 'accounts/signin.html'
    
    def get(self, request):
        signin = self.form_class()
        context = {
            'form': signin
        }
        return render(request, self.template_name, context)
    
    def post(self, request):
        signin = self.form_class(request.POST)
        if signin.is_valid():
            cd = signin.cleaned_data
            user = authenticate(
                username=cd['username'],
                password=cd['password']
            )
            
            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful', 'success')
                if self.next:
                    return redirect(self.next)
                return redirect('post:home')
            messages.error(request, 'username or password is wrong', 'warning')
        return render(request, self.template_name, {'form': signin})
        
class LogOutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        messages.success(request, 'Logged out successfully', 'success')
        return redirect('accounts:login')
    
    
class UserProfileView(LoginRequiredMixin,View):
    def get(self, request, user_id):
        is_following = False
        user = User.objects.get(pk=user_id)
        post = user.posts.all()
        relation = RelationUserModel.objects.filter(from_user=request.user, to_user=user.id)
        if relation.exists():
            is_following = True
        context = {
            'user': user,
            'post': post,
            'is_following': is_following
            
            
        }
        return render(request, 'accounts/profile.html', context)
    
    
class EditProfileView(LoginRequiredMixin, View):
    
    def setup(self, request, *args, **kwargs):
        self.user = get_object_or_404(User, pk=kwargs['user_id'])
        return super().setup(request, *args, **kwargs)
    
    def dispatch(self, request, *args, **kwargs):
        user = User.objects.get(pk=kwargs['user_id'])
        if request.user.id != user.id:
            messages.error(request, 'invalid', 'danger')
            return redirect('post:home')
        return super().dispatch(request, *args, **kwargs)
    
    template_name = 'accounts/edit-profile.html'
    from_class = UserEditProfileForm
    
    def get(self, request, *args, **kwargs):
        user = self.user
        update_user = self.from_class(instance=user)
        return render(request, self.template_name, {'user': update_user})
        
    def post(self, request, *args, **kwargs):
        user = self.user
        update_user = self.from_class(request.POST, instance=user)
        if update_user.is_valid():
            update_user.save()
            messages.success(request, 'successfly edit profile', 'success')
            return redirect('accounts:profile', request.user.id)
        return render(request, self.template_name, {'user': update_user})
        

# show form reset password and send form reset password to email account
class UserPasswordResetView(auth_views.PasswordResetView):
    template_name = 'accounts/password_reset_form.html'
    
    # redirect to who is page
    success_url = reverse_lazy('accounts:password_reset_done')
    
    # send content to email user
    email_template_name = 'accounts/password_reset_email.html'
    

# show success send email
class UserPasswordResetDoneView(auth_views.PasswordResetDoneView):
    template_name = 'accounts/password_reset_done.html'
    

# show fileds password
class UserPasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    # show form to user
    template_name = 'accounts/password_reset_confirm.html'
    success_url = reverse_lazy('accounts:password_reset_complete')
    
    
# show message after password reset
class PasswordResetComplateView(auth_views.PasswordResetCompleteView):
    template_name = 'accounts/password_reset_complete.html'
    

class UserFollowView(LoginRequiredMixin, View):
    # template_name = 'accounts/follow.html'
    
    def get(self, request, *args, **kwargs):
        user = User.objects.get(pk=kwargs['user_id'])
        relation = RelationUserModel.objects.filter(from_user=request.user, to_user=user)
        if relation.exists():
            messages.error(request, 'you follow this user', 'warning')
        else:
            RelationUserModel.objects.create(from_user=request.user, to_user=user)
            messages.success(request, 'follow', 'success')
        return redirect('accounts:profile', user.id)
        # return render(request, self.template_name, {'from_user': user, 'to_user': relation})
    
    
class UserUnfollowView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        user = User.objects.get(pk=kwargs['user_id'])
        relation = RelationUserModel.objects.filter(from_user=request.user, to_user=user)
        if relation.exists():
            relation.delete()
            messages.success(request, 'unfollow', 'success')
        return redirect('accounts:profile', user.id)
    

class NotifictionView(View):
    def get(self, request):
        notification = NotificationModel.objects.all()
        return render(request, 'accounts/notification.html', {'notification': notification})
        
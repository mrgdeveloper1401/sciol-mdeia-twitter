from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from .models import User
from .form import UserCreationForms, UserChangeForms, UserSignIn, UserSignUpForm
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
                return redirect('post:home')
            messages.error(request, 'username or password is wrong', 'warning')
        return render(request, self.template_name, {'form': signin})
        
class LogOutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        messages.success(request, 'Logged out successfully', 'success')
        return redirect('accounts:login')
    
    
class UserProfileView(View):
    def get(self, request, user_id):
        user = User.objects.get(pk=user_id)
        context = {
            'user': user,
            
        }
        return render(request, 'accounts/profile.html', context)
    

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
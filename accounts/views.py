from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from .models import User
from .form import UserCreationForms, UserChangeForms, UserSignIn, UserSignUpForm
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


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
    form_class = UserSignIn
    template_name = 'accounts/signin.html'
    def get(self, request):
        signin = self.form_class()
        context = {
            'signin': signin
        }
        return render(request, self.template_name, context)
    
    def post(self, request):
        signin = self.form_class(request.POST)
        if signin.is_valid():
            ...
            
# class SignInMobileView(View):
#     form_class = UserSignIn
#     template_name = 'accounts/signin_mobile.html'
#     def get(self, request):
#         signin = self.form_class()
#         context = {
#             'signin': signin
#         }
#         return render(request, self.template_name, context)
    
#     def post(self, request):
#         signin = self.form_class(request.POST)
#         if signin.is_valid():
#             ...
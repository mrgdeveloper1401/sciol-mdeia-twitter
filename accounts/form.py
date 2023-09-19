from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import User, OtpCode
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import AuthenticationForm
from django.core import validators


class UserCreationForms(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('email', 'full_name')
            
    def clean(self):
        cd = super().clean()
        password1 = cd.get('password1')
        password2 = cd.get('password2')
        if password1 and password2 and password1 != password2:
            raise ValidationError('password must be the same')
        
    def clean_email(self):
        cd = self.cleaned_data
        if User.objects.filter(email=cd['email']).exists():
            raise ValidationError('this email is already in exisits')
        return cd['email']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

    
class UserChangeForms(forms.ModelForm):
    password = ReadOnlyPasswordHashField(
        label=_("Password"),
        help_text=_(
            "Raw passwords are not stored, so there is no way to see this "
            "user’s password, but you can change the password using "
            '<a href="../password">this form</a>.'
        ),)
    class Meta:
        model = User
        fields = ('username','email', 'mobile_phone', 'full_name', 'last_login')
        
        
class UserSignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'enter Password'}))
    password2 = forms.CharField(label='confrim password',widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'enter confirm password'}))

    class Meta:
        model = User
        fields = ('email', 'full_name')
        
        widgets = {
            # 'mobile_phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter phone number'}),
            # 'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'enter email address'}),
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter full name'}),
            # 'birthday': forms.TextInput(attrs={'class': 'form-control'}),

        }
        
        labels = {
            # 'mobile_phone': 'mobile phone',
            # 'username': 'username',
            'email': 'email',
            'full_name': 'full name',
            # 'birth_day': 'birth day',

        }
        
        
    def clean(self):
        cd = super().clean()
        password1 = cd.get('password')
        password2 = cd.get('password2')
        if password1 and password2 and password1 != password2:
            raise ValidationError('password and password1 must be the same')
            
    def clean_email(self):
        cd = self.cleaned_data
        if User.objects.filter(email=cd['email']).exists():
            raise ValidationError('this email is already in exisits')
        return cd['email']
    
    # def clean_mobile_phone(self):
    #     cd = self.cleaned_data
    #     if User.objects.filter(mobile_phone=cd['mobile_phone']).exists():
    #         raise ValidationError('this mobile_phone is already in exisits')
    #     return cd['mobile_phone']
    
    # def clean_username(self):
    #     cd = self.cleaned_data
    #     if User.objects.filter(username=cd['username']).exists():
    #        raise ValidationError('this username is already in exisits')
    #     return cd['username']
        
class UserSignIn(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter username or email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'enter password'}))

# class UserSignIn(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ('username', 'password')
    
#     widgets = {
#         'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter username or email'}),
#         'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'enter your password'})
#     }


class UserEditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'full_name', 'mobile_phone', 'gender_choose')
        

class ActiveForm(forms.ModelForm):
    model = OtpCode
    fields = '__all__'
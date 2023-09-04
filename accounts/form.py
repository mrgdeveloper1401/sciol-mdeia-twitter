from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class UserCreationForms(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'mobile_phone', 'full_name')
        
            
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] and cd['password2'] and cd['password1'] != cd['password2']:
            raise ValidationError('password1 must be same')
        return cd['password2']
            
    def clean_email(self):
        cd = self.cleaned_data
        if User.objects.filter(email=cd['email']).exists():
            raise ValidationError('this email is already in exisits')
        return cd['email']
    
    def clean_mobile_phone(self):
        cd = self.cleaned_data
        if User.objects.filter(mobile_phone=cd['mobile_phone']).exists():
            raise ValidationError('this mobile_phone is already in exisits')
        return cd['mobile_phone']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
            # if hasattr(self, "save_m2m"):
            #     self.save_m2m()
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
        fields = ('username','email', 'mobile_phone', 'full_name', 'last_login', 'update_at')
        
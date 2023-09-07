from django import forms
from .models import PostModel


class PostCreateUpdateForm(forms.ModelForm):
    
    class Meta:
        model = PostModel
        fields = ('body', )
        
# class PostCreateform(forms.ModelForm):
#     class Meta:
#         model = PostModel
#         fields = ('body', )
        
from django import forms
from .models import PostModel


class PostUpdateForm(forms.ModelForm):
    
    class Meta:
        model = PostModel
        fields = ('body', )
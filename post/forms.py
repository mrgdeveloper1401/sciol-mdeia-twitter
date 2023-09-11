from django import forms
from .models import CommentModel, PostModel


class PostCreateUpdateForm(forms.ModelForm):
    
    class Meta:
        model = PostModel
        fields = ('body', )
        
# class PostCreateform(forms.ModelForm):
#     class Meta:
#         model = PostModel
#         fields = ('body', )


class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        fields = ('body', )
        
        widgets = {
            'body': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'type comment'}),
        }
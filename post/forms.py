from django import forms
from .models import CommentModel, PostModel


class PostCreateUpdateForm(forms.ModelForm):
    
    class Meta:
        model = PostModel
        fields = ('body', )
        
        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control w-75', 'placeholder': 'enetr text'})
            }

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
    
    
class PostSearchForms(forms.Form):
    search = forms.CharField(label='search post')
    
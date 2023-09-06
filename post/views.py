from django.shortcuts import render, redirect
from django.views import View
from .models import PostModel

class HomeView(View):
    form_class = ''
    template_name = 'post/home.html'
    
    def get(self, requet):
        post = PostModel.objects.all()
        return render(requet, self.template_name, {'post': post})
    


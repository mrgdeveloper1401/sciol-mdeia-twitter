from django.shortcuts import render, redirect
from django.views import View


class HomeView(View):
    def get(self, requet):
        return render(requet, 'post/home.html')
    


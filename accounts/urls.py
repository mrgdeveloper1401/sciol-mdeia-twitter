from django.urls import path
from . import views


app_name = 'accounts'
urlpatterns = [
    path('signin/', views.SignInView.as_view(), name='login'),
    # path('signin/mobile/', views.SignInMobileView.as_view(), name='login_mobile'),
    path('signup/', views.UserSignupView.as_view(), name='logup'),
    path('logout/', views.LogOutView.as_view(), name='logout'),
    
    
    
]

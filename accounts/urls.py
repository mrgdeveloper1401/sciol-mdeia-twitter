from django.urls import path
from . import views


app_name = 'accounts'
urlpatterns = [
    path('signin/', views.SignInView.as_view(), name='login'),
    # path('signin/mobile/', views.SignInMobileView.as_view(), name='login_mobile'),
    path('signup/', views.UserSignupView.as_view(), name='logup'),
    path('logout/', views.LogOutView.as_view(), name='logout'),
    path('profile/<int:user_id>/', views.UserProfileView.as_view(), name='profile'),
    # path('profile/<int:user_id>/<str:slug_id>/', views.UserProfileView.as_view(), name='profile_post'),
    path('reset/', views.UserPasswordResetView.as_view(), name='password_reset'),
    path('reset/done/', views.UserPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('confirm/<uidb64>/<token>/', views.UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('confirm/complete/', views.PasswordResetComplateView.as_view(), name='password_reset_complete'),
    path('follow/<int:user_id>/', views.UserFollowView.as_view(), name='user_follow'),
    path('unfollow/<int:user_id>/', views.UserUnfollowView.as_view(), name='user_unfollow'),
    
    
]

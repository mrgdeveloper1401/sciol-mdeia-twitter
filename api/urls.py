from django.urls import path
from api.views.accounts import SignUpApiView
from api.views.comments import *
from api.views.home import HomeView
from rest_framework.authtoken import views as auth_views
from api.views.posts import *


app_name = 'api'
urlpatterns = [
    path('signup/', SignUpApiView.as_view(), name='signup_api'),
    path('auth-token/', auth_views.obtain_auth_token, name='auth_token'),
    path('home/', HomeView.as_view(), name='home'),
    path('create-posts/', PostCreateApiView.as_view(), name='post_create'),
    path('show-post/', PostGetApiView.as_view(), name='show-post'),
    path('update-post/', PostUpdateApiView.as_view(), name='update-post'),
    path('delete-post/', PostDeleteApiview.as_view(), name='update-post'),
    path('create-comments/', CommentsCreateApiView.as_view(), name='comment_create_api'),
    path('show-comments/', CommetsGetApiView.as_view(), name='comment_create_api'),
    path('update-comments/', CommetsUpdateApiView.as_view(), name='update_comments'),
    path('delete-comments/', CommetsDeleteApiView.as_view(), name='delete-comments'),
    
    
    
]

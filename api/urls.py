from django.urls import path
from api.views.accounts import SignUpApiView, ProfileApiView
from api.views.comments import *
from api.views.home import HomeView
from rest_framework.authtoken import views as auth_views
from api.views.posts import *


app_name = 'api'
urlpatterns = [
    path('signup/', SignUpApiView.as_view(), name='signup_api'),
    path('profile/<int:user_id>/', ProfileApiView.as_view(), name='profile'),
    path('auth-token/', auth_views.obtain_auth_token, name='auth_token'),
    path('home/', HomeView.as_view(), name='home'),
    path('create-posts/', PostCreateApiView.as_view(), name='post_create'),
    path('show-posts/', PostGetApiView.as_view(), name='show-post'),
    path('update-posts/<int:post_id>/', PostUpdateApiView.as_view(), name='update-post'),
    path('delete-posts/<int:post_id>/', PostDeleteApiview.as_view(), name='update-post'),
    path('create-comments/', CommentsCreateApiView.as_view(), name='comment_create_api'),
    path('show-comments/', CommetsGetApiView.as_view(), name='comment_create_api'),
    path('update-comments/<int:comment_id>/', CommetsUpdateApiView.as_view(), name='update_comments'),
    path('delete-comments/<int:comment_id>/', CommetsDeleteApiView.as_view(), name='delete-comments'),
    
    
    
]

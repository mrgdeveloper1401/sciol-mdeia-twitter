from django.urls import path
from api.views.accounts import SignUpApiView
from api.views.comments import CommentsCreateApiView
from api.views.home import HomeView
from rest_framework.authtoken import views as auth_views
from api.views.posts import PostCreateApiView


app_name = 'api'
urlpatterns = [
    path('signup/', SignUpApiView.as_view(), name='signup_api'),
    path('auth-token/', auth_views.obtain_auth_token, name='auth_token'),
    path('create-comment/', CommentsCreateApiView.as_view(), name='comment_create_api'),
    path('home/', HomeView.as_view(), name='home'),
    path('create-post/', PostCreateApiView.as_view(), name='post_create'),
    
    
    
    
]

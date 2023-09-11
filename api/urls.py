from django.urls import path
from api.views.accounts import SignUpApiView
from rest_framework.authtoken import views as auth_views


app_name = 'api'
urlpatterns = [
    path('signup/', SignUpApiView.as_view(), name='signup_api'),
    path('auth-token/', auth_views.obtain_auth_token, name='auth_token'),

    
    
]

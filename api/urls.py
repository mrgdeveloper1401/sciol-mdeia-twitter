from django.urls import path
from api.views.accounts import SignUpApiView 


urlpatterns = [
    path('signup/', SignUpApiView.as_view(), name='signup_api')
]

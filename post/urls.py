from django.urls import path
from . import views



app_name = 'post'
urlpatterns = [
    path("", views.HomeView.as_view(), name='home'),
    path('details/<int:post_id>/<str:post_slug>/', views.PostDetailsView.as_view(), name='post_details'),
    path('details/delete/<int:post_id>/', views.PostDeleteView.as_view(), name='delete_post')
    
]

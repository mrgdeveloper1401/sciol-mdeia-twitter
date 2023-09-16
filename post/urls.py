from django.urls import path
from . import views



app_name = 'post'
urlpatterns = [
    path("", views.HomeView.as_view(), name='home'),
    path('details/<int:post_id>/<str:post_slug>/', views.PostDetailsView.as_view(), name='post_details'),
    # path('detailsss/<int:comment_id>/')
    path('details/delete/<int:post_id>/', views.PostDeleteView.as_view(), name='delete_post'),
    path('details/update/<int:post_id>/', views.UpdatePostView.as_view(), name='update_post'),
    path('create/<int:user_id>/', views.PostCreateView.as_view(), name='post_create'),
    path('like/<int:post_id>/', views.RelationPostLikeView.as_view(), name='like'),
    path('dislike/<int:post_id>/', views.RelationPostDislikeView.as_view(), name='dislike'),

]

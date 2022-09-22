from django.urls import path, include

from . import views

app_name = 'newzAPI'
urlpatterns = [
    # Landing page URLS
    path('posts/', views.LatestNewsAPIView.as_view(), name="posts"),
    path('post/<int:post_id>/', views.NewsAPIView.as_view(), name="post")
]
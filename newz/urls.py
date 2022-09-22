from django.urls import path
from . import views


app_name = 'newz'
urlpatterns = [
    # Landing page URLS
    path('', views.home, name="home"),
    path('<int:id>', views.post, name="post"),
]
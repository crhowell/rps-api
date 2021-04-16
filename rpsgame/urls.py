from django.urls import path

from . import views


urlpatterns = [
    path('games', views.all_games, name='games'),
]

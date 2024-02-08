# palindrome_game_api/urls.py
from django.urls import include, path
from . import views


urlpatterns = [
   # path('', views.index),  # Add a view for the root URL
  #  path('', include('palindrome_game_api.urls')),  # Include API URLs
    path('games/create/', views.create_game),
    path('games/<uuid:game_id>/board/', views.get_board),
    path('games/<uuid:game_id>/board/<str:char>/', views.update_board),
    path('users/create/', views.create_user),
    path('users/<int:user_id>/delete/', views.delete_user),
    path('users/<int:user_id>/update/', views.update_user),
    path('games/list/', views.list_games),
]
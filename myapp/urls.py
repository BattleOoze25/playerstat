from django.urls import path
from . import views
urlpatterns = [
    path('api/v1/get_player_average/', views.get_player_average, name="get_player_average"),
]
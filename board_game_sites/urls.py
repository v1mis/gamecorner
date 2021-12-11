#URL PATTERNS FOR board_game_sites

from django.urls import path
from . import views

app_name = 'board_game_sites'
urlpatterns = [
    #HOMEPAGE
    path('', views.index, name = 'index'),

    #A PAGE THAT SHOWS ALL GAMES
    path('games/', views.games, name = 'games'),

    #PAGE FOR AN INDIVIDUAL GAME
    path('games/<int:game_id>/', views.game, name = 'game'),

    #PAGE FOR ADDING A NEW GAME
    path('new_game/', views.new_game, name='new_game'),

]
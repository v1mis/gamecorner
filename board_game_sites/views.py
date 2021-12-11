from django.shortcuts import render, redirect
from board_game_sites.forms import GameForm

from board_game_sites.models import Boardgame

#HOMEPAGE
def index(request):
    return render(request, 'board_game_sites/index.html')

#A PAGE THAT SHOWS ALL GAMES
def games(request):
    games = Boardgame.objects.order_by('date_added')
    context = {'games': games}
    return render(request, 'board_game_sites/games.html', context)

#PAGE FOR AN INDIVIDUAL GAME
def game(request, game_id):
    game = Boardgame.objects.get (id=game_id)
    info = game.info_set.order_by('-date_added')
    context = {'game':game, 'info':info}
    return render(request, 'board_game_sites/game.html', context)

#PAGE FOR A ADDING A NEW GAME
def new_game(request):
    if request.method != 'POST':
        form = GameForm()
    
    else:
        form = GameForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('board_game_sites:games')

    context = {'form':form}
    return render(request, 'board_game_sites/new_game.html', context)
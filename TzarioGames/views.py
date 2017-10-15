from django.http import HttpResponse
from django.template import loader

from .models import Game

def index(request):
    unformat_game_list = Game.objects.all()
    format_game_list = []
    counter = 0
    temp_game_list = []
    for game in unformat_game_list:

        if counter == 2:
            temp_game_list.append(game)
            format_game_list.append(temp_game_list)
            temp_game_list = []
            counter = 0
        else:
            temp_game_list.append(game)
            counter+=1
    format_game_list.append(temp_game_list)
    template = loader.get_template('TzarioGames/index.html')
    context = {
        'format_game_list': format_game_list,
    }
    return HttpResponse(template.render(context, request))


def game(request, game_name):
    template = loader.get_template('TzarioGames/game.html')
    game = Game.objects.get(game_name=game_name)
    context = {'game': game}
    return HttpResponse(template.render(context, request))


def about(request):
    template = loader.get_template('TzarioGames/about.html')
    context = {}
    return HttpResponse(template.render(context, request))


def contact(request):
    template = loader.get_template('TzarioGames/contact.html')
    context = {}
    return HttpResponse(template.render(context, request))

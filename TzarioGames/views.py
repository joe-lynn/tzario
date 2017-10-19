from django.http import HttpResponse
from django.template import loader

from .models import Game

def index(request):
    unformat_game_list = Game.objects.all()
    format_game_list = []
    unformat_mobile_list = Game.objects.all()
    format_mobile_list = []
    unformat_shooter_list = Game.objects.all()
    format_shooter_list = []
    unformat_freeworld_list = Game.objects.all()
    format_freeworld_list = []
    unformat_strategy_list = Game.objects.all()
    format_strategy_list = []
    unformat_racing_list = Game.objects.all()
    format_racing_list = []

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

    counter = 0
    temp_game_list = []
    for game in unformat_mobile_list:
        if(game.game_category == "mobile"):
            if counter == 2:
                temp_game_list.append(game)
                format_mobile_list.append(temp_game_list)
                temp_game_list = []
                counter = 0
            else:
                temp_game_list.append(game)
                counter += 1
    format_mobile_list.append(temp_game_list)

    counter = 0
    temp_game_list = []
    for game in unformat_shooter_list:
        if (game.game_category == "shooter"):
            if counter == 2:
                temp_game_list.append(game)
                format_shooter_list.append(temp_game_list)
                temp_game_list = []
                counter = 0
            else:
                temp_game_list.append(game)
                counter += 1
    format_shooter_list.append(temp_game_list)

    counter = 0
    temp_game_list = []
    print(unformat_freeworld_list)
    for game in unformat_freeworld_list:
        print(game)
        print(game.game_category)
        if (game.game_category == "freeworld"):
            if counter == 2:
                temp_game_list.append(game)
                format_freeworld_list.append(temp_game_list)
                temp_game_list = []
                counter = 0
            else:
                temp_game_list.append(game)
                counter += 1
    format_freeworld_list.append(temp_game_list)

    counter = 0
    temp_game_list = []
    for game in unformat_strategy_list:
        if (game.game_category == "strategy"):
            if counter == 2:
                temp_game_list.append(game)
                format_strategy_list.append(temp_game_list)
                temp_game_list = []
                counter = 0
            else:
                temp_game_list.append(game)
                counter += 1
    format_strategy_list.append(temp_game_list)

    counter = 0
    temp_game_list = []
    for game in unformat_racing_list:
        if (game.game_category == "racing"):
            if counter == 2:
                temp_game_list.append(game)
                format_racing_list.append(temp_game_list)
                temp_game_list = []
                counter = 0
            else:
                temp_game_list.append(game)
                counter += 1
    format_racing_list.append(temp_game_list)

    template = loader.get_template('TzarioGames/index.html')
    context = {
        'format_game_list': format_game_list,
        'format_mobile_list': format_mobile_list,
        'format_freeworld_list': format_freeworld_list,
        'format_strategy_list': format_strategy_list,
        'format_racing_list': format_racing_list,
        'format_shooter_list': format_shooter_list,
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

from django.http import HttpResponse
from django.template import loader

from .models import Game

def index(request):
    unformat_game_list = Game.objects.all()
    unformat_mobile_list = []
    unformat_freeworld_list = []
    unformat_strategy_list = []
    unformat_racing_list = []
    unformat_shooter_list = []

    for game_obj in unformat_game_list:

        if game_obj.game_category.category_name == "mobile":
            unformat_mobile_list.append(game_obj)

        if game_obj.game_category.category_name == "freeworld":
            unformat_freeworld_list.append(game_obj)

        if game_obj.game_category.category_name == "strategy":
            unformat_strategy_list.append(game_obj)

        if game_obj.game_category.category_name == "racing":
            unformat_racing_list.append(game_obj)

        if game_obj.game_category.category_name == "shooter":
            unformat_shooter_list.append(game_obj)

    template = loader.get_template('TzarioGames/index.html')
    context = {
        'unformat_game_list': unformat_game_list,
        'unformat_mobile_list': unformat_mobile_list,
        'unformat_freeworld_list': unformat_freeworld_list,
        'unformat_strategy_list': unformat_strategy_list,
        'unformat_racing_list': unformat_racing_list,
        'unformat_shooter_list': unformat_shooter_list,
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

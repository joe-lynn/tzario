from django.http import HttpResponse
from django.template import loader

from .models import Game


def index(request):
    unformat_game_list = Game.objects.all()
    format_game_list = []
    unformat_mobile_list = Game.objects.all()
    format_mobile_list = []
    unformat_freeworld_list = Game.objects.all()
    format_freeworld_list = []
    unformat_strategy_list = Game.objects.all()
    format_strategy_list = []
    unformat_racing_list = Game.objects.all()
    format_racing_list = []
    unformat_shooter_list = Game.objects.all()
    format_shooter_list = []

    counter = 0
    mobile_counter = 0
    freeworld_counter = 0
    strategy_counter = 0
    racing_counter = 0
    shooter_counter = 0

    temp_game_list = []
    mobile_temp_game_list = []
    freeworld_temp_game_list = []
    strategy_temp_game_list = []
    racing_temp_game_list = []
    shooter_temp_game_list = []

    for game_obj in unformat_game_list:
        if counter == 2:
            temp_game_list.append(game_obj)
            format_game_list.append(temp_game_list)
            temp_game_list = []
            counter = 0
        else:
            temp_game_list.append(game_obj)
            counter += 1

        if game_obj.game_category.category_name == "mobile":
            if mobile_counter == 2:
                mobile_temp_game_list.append(game_obj)
                format_mobile_list.append(mobile_temp_game_list)
                mobile_temp_game_list = []
                mobile_counter = 0
            else:
                mobile_temp_game_list.append(game_obj)
                mobile_counter += 1

        if game_obj.game_category.category_name == "freeworld":
            if freeworld_counter == 2:
                freeworld_temp_game_list.append(game_obj)
                format_freeworld_list.append(freeworld_temp_game_list)
                freeworld_temp_game_list = []
                freeworld_counter = 0
            else:
                freeworld_temp_game_list.append(game_obj)
                freeworld_counter += 1

        if game_obj.game_category.category_name == "strategy":
            if strategy_counter == 2:
                strategy_temp_game_list.append(game_obj)
                format_strategy_list.append(strategy_temp_game_list)
                strategy_temp_game_list = []
                strategy_counter = 0
            else:
                strategy_temp_game_list.append(game_obj)
                strategy_counter += 1

        if game_obj.game_category.category_name == "racing":
            if racing_counter == 2:
                racing_temp_game_list.append(game_obj)
                format_racing_list.append(racing_temp_game_list)
                racing_temp_game_list = []
                racing_counter = 0
            else:
                racing_temp_game_list.append(game_obj)
                racing_counter += 1

        if game_obj.game_category.category_name == "shooter":
            if shooter_counter == 2:
                shooter_temp_game_list.append(game_obj)
                format_shooter_list.append(shooter_temp_game_list)
                shooter_temp_game_list = []
                shooter_counter = 0
            else:
                shooter_temp_game_list.append(game_obj)
                shooter_counter += 1

    format_game_list.append(temp_game_list)
    format_mobile_list.append(mobile_temp_game_list)
    format_freeworld_list.append(freeworld_temp_game_list)
    format_strategy_list.append(strategy_temp_game_list)
    format_racing_list.append(racing_temp_game_list)
    format_shooter_list.append(shooter_temp_game_list)

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

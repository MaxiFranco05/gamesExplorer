from gamesExplorer.plataformas.steam.utils import *

def get_steam_games(is_discount = False):
    games_list = get_games(is_discount)
    games = []
    for game in games_list:
        game_obj = {}
        game_obj["title"] = get_title(game)
        game_obj["release"] = get_release_date(game)
        game_obj["price"] = get_price(game)
        game_obj["discount"] = get_discount(game)
        game_obj["rating"] = get_rating(game)
        games.append(game_obj)
    return games
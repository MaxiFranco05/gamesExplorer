from gamesExplorer import GamesManager

juegos = GamesManager('steam', True)
print(juegos.get_config())
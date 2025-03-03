from gamesExplorer.plataformas.steam import get_steam_games

class GamesManager:
    def __init__(self, plataforma, descuento):
        self.platf = plataforma
        self.desc = descuento
        self.games = self.get_platform_games()
    
    def get_platform_games(self):
        if self.platf.lower() == 'steam':
            return get_steam_games(self.desc)
        else:
            return None
    
    def get_config(self):
        config = {'plataforma': self.platf,
                  'descuento': 'Si' if self.desc else 'No'}
        return config
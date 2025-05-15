from core.manager import Manager
from games.wotr.game import Game
from games.wotr.config import manager_config, game_config

def create_manager(game : Game):
    return Manager(
        config = manager_config,
        game = game
    )

def create_game():
    return Game(
        config = game_config
    )
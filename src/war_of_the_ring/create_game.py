from core.game_manager import GameManager
from war_of_the_ring.config import game_config

def create_game():
    return GameManager(
        config = game_config
    )
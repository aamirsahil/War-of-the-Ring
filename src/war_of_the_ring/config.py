from model import DisplayConfig, GameConfig
from war_of_the_ring.game import Game

display_data = {
        "width" : 800,
        "height" : 600,
        "screen_depth" : 32,
        "fullscreen" : False
    }
display_config = DisplayConfig(**display_data)

game = Game()

game_data = {
    "title" : "War of the Ring",
    "fps" : 60,
    "game" : game,
    "display_config" : display_config
}
game_config = GameConfig(**game_data)
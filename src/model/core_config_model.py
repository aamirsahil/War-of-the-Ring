from dataclasses import dataclass
from war_of_the_ring.game import Game

# data model for defining display
@dataclass
class DisplayConfig:
    width : int
    height : int
    fullscreen : bool
    screen_depth : int

# data model for game
@dataclass
class GameConfig:
    title : str
    fps : int
    game : Game
    display_config : DisplayConfig
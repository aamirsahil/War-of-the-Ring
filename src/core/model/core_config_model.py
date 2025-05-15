from dataclasses import dataclass

# data model for defining display
@dataclass
class DisplayConfig:
    width : int
    height : int
    fullscreen : bool
    screen_depth : int

# data model for game
@dataclass
class ManagerConfig:
    title : str
    fps : int
    display_config : DisplayConfig
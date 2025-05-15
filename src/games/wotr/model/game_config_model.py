from dataclasses import dataclass
from games.wotr.model import Scene

@dataclass
class MapConfig:
    map_loc : str

@dataclass
class GameConfig:
    turn : int
    scene : Scene
    map_config : MapConfig
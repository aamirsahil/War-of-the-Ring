from typing import Optional

# interface modules
from interface_api import IGame, IDrawGraphics, IEventTypes, IDisplay

# game modules
from games.wotr.model import GameConfig
from games.wotr.map import Map
from games.wotr.input_manager import InputManager
from games.wotr.level_manager import LevelManagaer

class Game(IGame):
    def __init__(self, config : GameConfig):
        self.current_turn = config.turn
        self.current_scene = config.scene
        self.map = Map(config=config.map_config)
        self.input_manager = InputManager()
        self.level_manager = LevelManager()

    def start(self, display : IDisplay):
        # setup level data
        
        map = IDrawGraphics(
            id="map",
            asset_loc=self.map.map_loc,
            pos_offset=(100, 0),
            view_area=(0, 0, 500, 500)
        )
        display.load(
            surface_data=map
        )
    
    def update(self, event : Optional[IEventTypes]):
        self.input_manager.process_event(event = event)

    def render(self, display : IDisplay):
        display.draw(id="map")
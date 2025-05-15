from typing import Optional
import pygame

# interface modules
from interface_api import IGame, IEventTypes, IDisplay, IDrawGraphics

# game modules
from games.wotr.model import Scene, GameConfig
from games.wotr.map import Map
from games.wotr.input_manager import InputManager

class Game(IGame):
    def __init__(self, config : GameConfig):
        self.current_turn = config.turn
        self.current_scene = config.scene
        self.map = Map(config=config.map_config)
        self.input_manager = InputManager()

    def start(self, display : IDisplay):
        map = IDrawGraphics(
            id="map",
            asset_loc=self.map.map_loc,
            pos_offset=(0, 0),
            view_area=(0, 0, 300, 300)
        )
        display.load(
            surface=map
        )
    
    def update(self, event : Optional[IEventTypes]):
        self.input_manager.process_event(event = event)

    def render(self, display : IDisplay):
        display.draw(id="map")
from typing import List
from random import randint

from interface_api import ILevel, IDisplay, IEventTypes, IGameImage

class OpeningMenu(ILevel):
    def __init__(self, config):
        self.background = self._setup_background(config)

    def load(self, display : IDisplay):
        pass

    def update(self, event : IEventTypes):
        return super().update(event)
    
    def render(self, display : IDisplay):
        return super().render(display)
    
    def _setup_background(self, config) -> List[]:
        num_of_images = len(config.background_images)
        random_num = randint(0, num_of_images-1)
        asset_loc = config.background_images[random_num]
        

from typing import List

from games.wotr.model import Scene

from interface_api import IDrawGraphics

class LevelManager:
    def __init__(self):
        pass
    def level_structure(self, current_level : Scene) -> List[IDrawGraphics]:
        if current_level == Scene.Menu:
            # elements in the screen
            background = IDrawGraphics()
            title = IDrawGraphics()
            offline_button = ""
            online_button = ""
        elif current_level == Scene.Map:
            pass
from games.wotr.model import MapConfig

class Map:
    def __init__(self, config : MapConfig):
        self.map_loc = config.map_loc
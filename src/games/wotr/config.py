from core.model import DisplayConfig, ManagerConfig
from games.wotr.model import MapConfig, GameConfig, Scene

# game data
map_data = {
    "map_loc" : "src/games/wotr/assets/map/map_cut.png"
}
map_config = MapConfig(**map_data)

game_data = {
    "turn" : 0,
    "scene" : Scene.Map,
    "map_config" : map_config
}
game_config = GameConfig(**game_data)

# core data
display_data = {
        "width" : 800,
        "height" : 600,
        "screen_depth" : 32,
        "fullscreen" : False
    }
display_config = DisplayConfig(**display_data)

manager_data = {
    "title" : "War of the Ring",
    "fps" : 60,
    "display_config" : display_config
}
manager_config = ManagerConfig(**manager_data)
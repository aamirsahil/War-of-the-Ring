from model import DisplayConfig, GameConfig

display_data = {
        "width" : 1920,
        "height" : 1080,
        "screen_depth" : 32,
        "fullscreen" : True
    }
display_config = DisplayConfig(**display_data)

game_data = {
    "title" : "War of the Ring",
    "fps" : 60, 
    "display_config" : display_config 
}
game_config = GameConfig(**game_data)
from core.game import Game
import config

def main():
    game = Game(
        config = config.game_config
        )
    game.run()
    print("Done, Thanks for playing")

if __name__=="__main__":
    main()
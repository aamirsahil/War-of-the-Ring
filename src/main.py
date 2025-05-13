from war_of_the_ring import config
from war_of_the_ring.game_manager import Game

def main():
    game = Game(
        config = config.game_config
        )
    game.run()
    print("Done, Thanks for playing")

if __name__=="__main__":
    main()
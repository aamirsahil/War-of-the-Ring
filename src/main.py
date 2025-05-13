from war_of_the_ring import game_config, create_game

def main():
    game = create_game()
    game.run()
    print("Done, Thanks for playing")

if __name__=="__main__":
    main()
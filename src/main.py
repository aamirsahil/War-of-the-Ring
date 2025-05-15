from games import create_game, create_manager

def main():
    game = create_game()
    manager = create_manager(game = game)
    
    manager.run()
    print("Done, Thanks for playing")

if __name__=="__main__":
    main()
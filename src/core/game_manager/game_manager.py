import pygame

from model import GameConfig

from core.display import Display
from core.quit import Quit

from interface_api import IGameManager

class GameManager(IGameManager):
    def __init__(self, config : GameConfig):
        self.title = config.title
        self.display = Display(config = config.display_config)
        self.clock = pygame.time.Clock()
        self.fps = config.fps
        self.running = True
        self.game = config.game

    def run(self):
        # main loop
        pygame.init()
        pygame.display.set_caption(self.title)
        self.game.start()

        while self.running:
            # event management
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            # self.game.update()
            # self.display.draw()

            # refresh screen
            pygame.display.flip()
            # tick clock
            self.clock.tick(60)
        
        # terminate the game
        pygame.quit()

import pygame

from model import GameConfig

from core.display import Display
from core.quit import Quit

class Game:
    def __init__(self, config : GameConfig):
        self.title = config.title
        self.quit = Quit()
        self.display = Display(config = config.display_config)
        self.clock = pygame.time.Clock()
        self.fps = config.fps
        self.running = True
        self.surfaces = []
        self.level = {}

    def run(self):
        # main loop
        pygame.init()
        pygame.display.set_caption(self.title)

        while self.running:
            # event management
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            
            # self.display.draw()

            # refresh screen
            pygame.display.flip()
            # tick clock
            self.clock.tick(60)
        
        # terminate the game
        pygame.quit()

import pygame

from core.model import ManagerConfig
from core.display import Display
from core.inputs import EventTranslator

from interface_api import IManager, IGame

class Manager(IManager):
    def __init__(self, config : ManagerConfig, game : IGame):
        self.title = config.title
        self.display = Display(config = config.display_config)
        self.event_translator = EventTranslator()
        self.clock = pygame.time.Clock()
        self.fps = config.fps
        self.running = True
        self.game = game

    def run(self):
        # main loop
        pygame.init()
        pygame.display.set_caption(self.title)
        self.game.start()

        while self.running:
            # event management
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False
                event_type = self.event_translator.translate(event = event)
                self.game.update(event = event_type)

            self.game.render(display = self.display)

            # refresh screen
            pygame.display.flip()
            # tick clock
            self.clock.tick(self.fps)
        
        # terminate the game
        pygame.quit()

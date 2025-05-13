import pygame

from model import DisplayConfig, DrawSurface

from core.display.scroll import Scroll
from core.display.zoom import Zoom

from typing import List, Dict

class Display:
    def __init__(self, config : DisplayConfig):
        self.WIDTH = config.width
        self.HEIGHT = config.height
        flag = pygame.FULLSCREEN if config.fullscreen else 0
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT), flag, config.screen_depth)
        # self.map = Map()
        # self.scroll = Scroll()
        # self.zoom = Zoom()

    def draw(self, draw_element : List[DrawSurface]):
        for element in draw_element:
            self._draw_surface(element = element)

    def _draw_surface(self, element : DrawSurface):
        self.screen.blit(
            source = element.surface,
            dest = element.pos_offset,
            area = element.view_rect
        )
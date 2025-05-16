import pygame
from typing import Dict

from core.model import DisplayConfig, DrawSurface

from interface_api import IDisplay, IDrawGraphics

class Display(IDisplay):
    """
    Handles screen related logic.

    Attributes:
        width (int) : screen width
        height (int) : screen height
        screen (pygame.Surface) : pygame screen element
        surfaces (Dict[str , DrawSurface]) : surfaces to draw

    Methods:
        - load(surface: IDrawGraphics): Add surface to self.surfaces.
        - unload(id: str): Remove element from self.surfaces.
        - draw(id: str): Draw surface from surfaces by referencing id.
        - draw_all(): Draw all elements in surfaces.
    """
    def __init__(self, config : DisplayConfig):
        self.width = config.width
        self.height = config.height
        flag = pygame.FULLSCREEN if config.fullscreen else 0
        self.screen = pygame.display.set_mode((self.width, self.height), flag, config.screen_depth)
        self.surfaces : Dict[str , DrawSurface] = {}

    def load(self, surface_data : IDrawGraphics):
        """
        Add surface data to self.sufaces
        Parameters:
            surface (IDrawGraphics) : surface data sent by game module
        """
        surface = pygame.image.load(surface_data.asset_loc)
        offset = surface_data.pos_offset
        view_rect = pygame.Rect(*surface_data.view_area)
        
        draw_surface = DrawSurface(
            surface = surface,
            pos_offset = offset,
            view_rect = view_rect
        )
        self.surfaces[surface_data.id] = draw_surface
    
    def unload(self, id : str):
        """
        Remove surface from self.surfaces
        Parameters:
            id (str) : surface id to remove
        """
        if id in self.surfaces:
            del self.surfaces[id]

    def draw(self, id : str):
        """
        Draw the surface[id] on self.screen
        Parameters:
            id (str) : surface id to draw
        """
        self.screen.blit(
            source = self.surfaces[id].surface,
            dest = self.surfaces[id].pos_offset,
            area = self.surfaces[id].view_rect
        )

    def draw_all(self):
        """
        Draw all surfaces in self.surfaces
        """
        for id,_ in self.surfaces.items():
            self.draw(id = id)
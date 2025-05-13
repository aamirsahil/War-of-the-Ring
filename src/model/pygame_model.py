from dataclasses import dataclass
import pygame

@dataclass
class DrawSurface:
    surface : pygame.Surface
    pos_offset : pygame.Rect
    view_rect : pygame.Rect

import pygame
from typing import Optional

from interface_api.core import IEventTypes

class EventTranslator:
    def __init__(self):
        self.dragging = False
        self.drag_start_pos = (0, 0)
        self.drag_threshold = 5 # distance the mouse should move to avoid triggering option

    def translate(self, event : pygame.event.Event) -> Optional[IEventTypes]:
        if event.type == pygame.MOUSEBUTTONDOWN:
            # check if select
            if event.button == 1:
                return IEventTypes.Select # left mouse button
            # check if drag start
            elif event.button == 3:
                self.dragging = True # dragging start
                self.drag_start_pos = event.pos
                return IEventTypes.Dragging
            # check if scroll in
            elif event.button == 4:
                return IEventTypes.ScrollIn
            # check if scroll out
            elif event.button == 5:
                return IEventTypes.ScrollOut
        
        if event.type == pygame.MOUSEBUTTONUP:
            # check if drag end
            if event.button == 3:
                self.dragging = False
                if pygame.math.Vector2(self.drag_start_pos).distance_to(pygame.math.Vector2(event.pos)) < self.drag_threshold:
                    return IEventTypes.Option
                else:
                    return IEventTypes.Dragging
            
        if event.type == pygame.MOUSEMOTION:
            # check if dragging
            if self.dragging:
                return IEventTypes.Dragging
            
        return None
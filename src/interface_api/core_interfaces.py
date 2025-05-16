from abc import ABC, abstractmethod

from .data_interfaces import IDrawGraphics

class IManager(ABC):
    @abstractmethod
    def run(self):
        pass

class IDisplay(ABC):
    """
    Methods:
        - load(surface: IDrawGraphics): Add surface to self.surfaces.
        - unload(id: str): Remove element from self.surfaces.
        - draw(id: str): Draw surface from surfaces by referencing id.
        - draw_all(): Draw all elements in surfaces.
    """
    @abstractmethod
    def load(self, surface_data : IDrawGraphics):
        """
        Add surface data to self.sufaces
        Parameters:
            surface (IDrawGraphics) : surface data sent by game module
        """
        pass
    def unload(self, id : str):
        """
        Remove surface from self.surfaces
        Parameters:
            id (str) : surface id to remove
        """
        pass
    def draw(self, id : str):
        """
        Draw the surface[id] on self.screen
        Parameters:
            id (str) : surface id to draw
        """
        pass
    def draw_all(self):
        """
        Draw all surfaces in self.surfaces
        """
        pass
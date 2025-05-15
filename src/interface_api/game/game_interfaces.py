from abc import ABC, abstractmethod
from typing import Optional, Tuple
from dataclasses import dataclass

from core.core_interfaces import IDisplay, IEventTypes

class IGame(ABC):
    @abstractmethod
    def start(self):
        pass
    def update(self, event : Optional[IEventTypes]):
        pass
    def render(self, display : IDisplay):
        pass

@dataclass
class IDrawGraphics:
    id : str
    asset_loc : str
    pos_offset : Tuple[int, int]
    view_area : Tuple[int, int, int, int]
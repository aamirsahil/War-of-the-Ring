from abc import ABC, abstractmethod
from typing import Optional

from .core_interfaces import IDisplay
from .data_interfaces import IEventTypes

class IGame(ABC):
    @abstractmethod
    def start(self, display : IDisplay):
        pass
    def update(self, event : Optional[IEventTypes]):
        pass
    def render(self, display : IDisplay):
        pass
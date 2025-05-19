from abc import ABC, abstractmethod
from typing import Optional

from .core_interfaces import IDisplay
from .data_interfaces import IEventTypes

class ILevel(ABC):
    @abstractmethod
    def start(self, display : IDisplay):
        pass
    
    @abstractmethod
    def load(self, display : IDisplay):
        pass

    @abstractmethod
    def update(self, event : Optional[IEventTypes]):
        pass
    
    @abstractmethod
    def render(self, display : IDisplay):
        pass
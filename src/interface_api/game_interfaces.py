from abc import ABC, abstractmethod

class IGame(ABC):
    @abstractmethod
    def start(self):
        pass
    def update(self):
        pass
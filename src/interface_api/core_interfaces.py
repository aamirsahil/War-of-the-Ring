from abc import ABC, abstractmethod

class IGameManager(ABC):
    @abstractmethod
    def run(self):
        pass
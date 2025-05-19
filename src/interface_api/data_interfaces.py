from dataclasses import dataclass
from typing import Tuple
from enum import Enum, auto

@dataclass
class IDrawGraphics:
    id : str
    asset_loc : str
    pos_offset : Tuple[int, int]
    view_area : Tuple[int, int, int, int]

@dataclass
class IGameImage:
    asset_loc : str
    opacity : int

class IEventTypes(Enum):
    Quit = auto()
    Select = auto()
    ScrollIn = auto()
    ScrollOut = auto()
    Dragging = auto()
    Option = auto()
from typing import Optional

from interface_api.core import IEventTypes

class InputManager:
    def __init__(self):
        pass
    def process_event(self, event : Optional[IEventTypes]):
        if event == IEventTypes.Select:
            print("Mouse Click")
        elif event == IEventTypes.ScrollIn:
            print("Scroll In")
        elif event == IEventTypes.ScrollOut:
            print("Scroll out")
        elif event == IEventTypes.Dragging:
            print("Dragging")
        elif event == IEventTypes.Option:
            print("Option")
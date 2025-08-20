from typing import Union, List, Dict, Any
from dataclasses import dataclass
from enum import Enum

class EventType(Enum):
    CLICK = "click"
    HOVER = "hover"
    KEYPRESS = "keypress"

@dataclass
class MouseEvent:
    x: int
    y: int
    button: str = "left"

@dataclass
class KeyEvent:
    key: str
    modifiers: List[str]

@dataclass
class CustomEvent:
    event_type: str
    data: Dict[str, Any]

def process_event(event: Union[MouseEvent, KeyEvent, CustomEvent, tuple]):
    """Advanced pattern matching example"""
    match event:
        case MouseEvent(x, y, button="left"):
            print(f"Left click at ({x}, {y})")
        
        case MouseEvent(x, y, button="right"):
            print(f"Right click at ({x}, {y})")
        
        case KeyEvent(key="Enter", modifiers=mods) if "Ctrl" in mods:
            print("Ctrl+Enter pressed")
        
        case KeyEvent(key=key, modifiers=mods) if len(mods) > 0:
            print(f"Modified key press: {'+'.join(mods + [key])}")
        
        case CustomEvent(event_type=EventType.HOVER.value, data={"duration": d}):
            print(f"Hovered for {d}ms")
        
        case (x, y) if isinstance(x, int) and isinstance(y, int):
            print(f"Coordinate tuple: ({x}, {y})")
        
        case _:
            print("Unknown event type")

# Usage examples
process_event(MouseEvent(100, 200, "left"))
process_event(KeyEvent("Enter", ["Ctrl", "Shift"]))
process_event(CustomEvent("click", {"duration": 500}))
process_event((50, 75))

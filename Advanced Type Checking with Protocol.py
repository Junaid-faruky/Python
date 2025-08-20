from typing import Protocol, runtime_checkable, TypeVar, List
from dataclasses import dataclass

@runtime_checkable
class Renderable(Protocol):
    def render(self) -> str: ...
    
    def get_width(self) -> int: ...
    
    def get_height(self) -> int: ...

T = TypeVar('T', bound=Renderable)

@dataclass
class TextBox:
    content: str
    width: int = 50
    height: int = 10
    
    def render(self) -> str:
        return f"TextBox: {self.content[:30]}..."
    
    def get_width(self) -> int:
        return self.width
    
    def get_height(self) -> int:
        return self.height

@dataclass
class Image:
    src: str
    width: int
    height: int
    
    def render(self) -> str:
        return f"Image: {self.src}"
    
    def get_width(self) -> int:
        return self.width
    
    def get_height(self) -> int:
        return self.height

class LayoutEngine:
    def __init__(self):
        self.elements: List[Renderable] = []
    
    def add_element(self, element: Renderable):
        if not isinstance(element, Renderable):
            raise TypeError("Element must be Renderable")
        self.elements.append(element)
    
    def render_all(self) -> str:
        total_width = max(elem.get_width() for elem in self.elements)
        result = ["=" * total_width]
        
        for elem in self.elements:
            rendered = elem.render()
            padding = (total_width - len(rendered)) // 2
            result.append(" " * padding + rendered)
        
        result.append("=" * total_width)
        return "\n".join(result)

# Usage
engine = LayoutEngine()
engine.add_element(TextBox("Hello, World!", width=60))
engine.add_element(Image("logo.png", width=80, height=40))

print(engine.render_all())
print(f"Is TextBox Renderable? {isinstance(TextBox('test'), Renderable)}")

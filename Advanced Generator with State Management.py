from typing import Generator, Optional, List, Any
from enum import Enum, auto

class GeneratorState(Enum):
    RUNNING = auto()
    PAUSED = auto()
    STOPPED = auto()

class StatefulGenerator:
    def __init__(self, data: List[Any]):
        self.data = data
        self.index = 0
        self.state = GeneratorState.RUNNING
        self._callbacks = []
    
    def __iter__(self) -> Generator[Any, None, None]:
        while self.index < len(self.data) and self.state != GeneratorState.STOPPED:
            if self.state == GeneratorState.PAUSED:
                yield None
                continue
            
            item = self.data[self.index]
            self.index += 1
            
            # Execute callbacks
            for callback in self._callbacks:
                callback(item, self.index)
            
            yield item
    
    def pause(self):
        self.state = GeneratorState.PAUSED
    
    def resume(self):
        self.state = GeneratorState.RUNNING
    
    def stop(self):
        self.state = GeneratorState.STOPPED
    
    def add_callback(self, callback):
        self._callbacks.append(callback)
    
    def rewind(self, steps: int = 1):
        self.index = max(0, self.index - steps)

# Usage
def log_callback(item, index):
    print(f"Processing item {index}: {item}")

gen = StatefulGenerator([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
gen.add_callback(log_callback)

for i, item in enumerate(gen):
    print(f"Received: {item}")
    if i == 2:
        gen.pause()
        print("Generator paused")
    elif i == 4:
        gen.resume()
        print("Generator resumed")
    elif i == 7:
        gen.stop()
        print("Generator stopped")
        break

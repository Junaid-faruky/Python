from abc import ABC, abstractmethod

class Shape(ABC): # Inherit from ABC

    @abstractmethod
    def area(self):
        """Calculate the area of the shape. Must be implemented by subclasses."""
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self): # Must be implemented
        return self.width * self.height

    def perimeter(self): # Must be implemented
        return 2 * (self.width + self.height)

# This will work
rect = Rectangle(5, 3)
print(rect.area())

# This will raise a TypeError because `area` is not implemented
class Circle(Shape):
    pass
# TypeError: Can't instantiate abstract class Circle with abstract methods area, perimeter

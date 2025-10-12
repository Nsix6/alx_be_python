import math

class Shape:
    """Base class for different shapes."""

    def area(self):
        raise NotImplementedError("Subclasses must implement this method")
    
class Rectangle(Shape):
    """A rectangle shape."""
    
    def __init__(self, width, length):
        self.width = width
        self.length = length
    
    def area(self):
        """Calculate the area of the rectangle."""
        return self.length * self.width
    
class Circle(Shape):
    """A circle shape."""
    
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        """Calculate the area of the circle."""
        return 3.14159 * (self.radius ** 2)
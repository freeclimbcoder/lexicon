import math
from math import pi 
from shape import Shape
class Circle(Shape):
    def __init__(self, radius: float) -> None:
        self._radius = radius

    def __str__(self) -> str:
        return  f'This is a circle with radius = {self.radius}, {super().__str__()}'

    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        """Sets the radius. Must be positive"""
        if value > 0:
            self._radius = value
        else:
            raise ValueError("Radius must be positive")

    def area(self) -> float:
        return self.radius**2*math.pi
    
    def perimeter(self):
        return self.radius*2*pi
    

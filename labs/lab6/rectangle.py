from shape import Shape

class  Rectangle(Shape):
    def __init__(self, length: float, width: float) -> None:
        self._length = length
        self._width = width

    def __str__(self) -> str:
        return f'This is a rectangle with length = {self.length}, width = {self.width}, {super().__str__()}'

    @property
    def length(self) -> float:
        return self._length
    
    @property
    def width(self) -> float:
        return self._width
    
    @length.setter
    def length(self, value) -> None:
        """Sets the length. Must be positive"""
        if value > 0:
            self._length = value
        else:
            raise ValueError("Length must be positive")
        
    @width.setter
    def width(self, value) -> None:
        """Sets the width. Must be positive"""
        if value > 0:
            self._width = value
        else:
            raise ValueError("Width must be positive")
    
    def area(self) -> float:
        return self.length*self.width
    
    def perimeter(self) -> float:
        return 2*(self.length+self.width)
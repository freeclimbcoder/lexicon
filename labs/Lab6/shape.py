class Shape():
    def __init__(self) -> None:
        pass

    def __str__(self) -> str:
        return f'area = {self.area()}, perimeter = {self.perimeter()}'
    
    def area(self):
        return
    
    def perimeter(self):
        return

class Circle(Shape):
    def __init__(self, radius: float) -> None:
        super().__init__()
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

    def area(self):
        return self.radius**2*3.14
    
    def perimeter(self):
        return self.radius*2*3.14
    

class  Rectangle(Shape):
    def __init__(self, length: float, width: float) -> None:
        super().__init__()
        self._length = length
        self._width = width

    def __str__(self) -> str:
        return f'This is a rectangle with length = {self.length}, width = {self.width}, {super().__str__()}'

    @property
    def length(self):
        return self._length
    
    @property
    def width(self):
        return self._width
    
    @length.setter
    def length(self, value):
        """Sets the length. Must be positive"""
        if value > 0:
            self._length = value
        else:
            raise ValueError("Length must be positive")
        
    @width.setter
    def width(self, value):
        """Sets the width. Must be positive"""
        if value > 0:
            self._width = value
        else:
            raise ValueError("Width must be positive")
    
    def area(self):
        return self.length*self.width
    
    def perimeter(self):
        return 2*(self.length+self.width)
    
class Triangle(Shape):
    def __init__(self, a: float, b: float, c: float) -> None:
        super().__init__()
        p = (a + b + c)/2
        if a < p and b < p and c < p:
            self._a = a
            self._b = b
            self._c = c
        else:
            raise ValueError('any side must be shorter than 1/2 of perimeter')

    def __str__(self) -> str:
        return f'This is a triangle with sides: a = {self.a}, b = {self.b}, c = {self.c}, {super().__str__()}'

    @property
    def a(self):
        return self._a
    
    @property
    def b(self):
        return self._b
    
    @property
    def c(self):
        return self._c
    
    @a.setter
    def a(self, value):
        """Sets the a side. Must be positive"""
        if value > 0:
            self._a = value
        else:
            raise ValueError("Side must be positive")

    @b.setter
    def b(self, value):
        """Sets the b side. Must be positive"""
        if value > 0:
            self._b = value
        else:
            raise ValueError("Side must be positive")
        
    @c.setter
    def c(self, value):
        """Sets the c side. Must be positive"""
        if value > 0:
            self._c = value
        else:
            raise ValueError("Side must be positive")
        
    def perimeter(self) -> float:
        return self.a + self.b + self.c
    
    def area(self) -> float:
        #S = √p · (p — a)(p — b)(p — c),
        p = self.perimeter()/2
        return p**(1/2)*(p-self.a)*(p-self.b)*(p-self.c)
    


c = Circle(1)
print(c)
print(c.area())
print(c.perimeter())

r = Rectangle(2,3)
print(r)
print(r.area())
print(r.perimeter())
r.length = 22
print(r.perimeter())

t = Triangle(1, 2, 2)
print(t)
print(t.perimeter())
print(t.area())
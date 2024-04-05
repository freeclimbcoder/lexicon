from shape import Shape

class Triangle(Shape):
    def __init__(self, a: float, b: float, c: float) -> None:
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
    def a(self) -> float:
        return self._a
    
    @property
    def b(self) -> float:
        return self._b
    
    @property
    def c(self) -> float:
        return self._c
    
    @a.setter
    def a(self, value) -> None:
        """Sets the a side. Must be positive"""
        if value > 0:
            self._a = value
        else:
            raise ValueError("Side must be positive")

    @b.setter
    def b(self, value) -> None:
        """Sets the b side. Must be positive"""
        if value > 0:
            self._b = value
        else:
            raise ValueError("Side must be positive")
        
    @c.setter
    def c(self, value) -> None:
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
        return (p*(p-self.a)*(p-self.b)*(p-self.c))**(1/2)
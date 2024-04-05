
from circle import Circle
from rectangle import Rectangle
from triangle import Triangle

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

t = Triangle(3, 4, 5)
print(t)
print(t.perimeter())
print(t.area())
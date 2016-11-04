import math

class Shape:
     def __init__(self, pos_x, pos_y):
         self.x = pos_x
         self.y = pos_y
     def area(self):
         # Not implemented in abstract base class
         pass

class Circle(Shape):
     def setRadius(self, r):
         self.radius = r
     def area(self):
         return math.pi * self.radius * self.radius

class Square(Shape):
     def setSide(self, s):
         self.side = s
     def area(self):
         return self.side * self.side


c1 = Circle(1, 4)
c1.setRadius(5)

c2 = Circle(6, 4)
c2.setRadius(3)

s1 = Square(10, 4)
s1.setSide(15)

s2 = Square(10, 14)
s2.setSide(5)

for shape in c1, c2, s1, s2:
     print(shape.area())


class math:
    def add(a,b):
        a.x = a + 1
        
    # def take_away(a,b):
    #     return a - b

class math2(math):
    def fun(a,b):
        a.bob = b
        return a.bob + b

# class test1(test):
#     def hi(a,b):

c1 = math2(5, 5)
c1.bob(5)

print(math())
print(math2.fun(5,5))
#print(math.take_away(10,5))
        

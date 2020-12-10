
#PPL Assignment 6 - shapes 
#MIS: 111903095
#Name: Shalaka Pawar
#Division : 2
import math
import turtle

class Shape:
    def Area(self):
        pass

    def Perimeter(self):
        pass


class Polygon(Shape):
    def __init__(self, n):
        self.num_of_sides = n

    def print_num_sides(self):
        print("Number of sides in given polygon = ", self.num_of_sides)

    def description(self):
        print("A polygon is a closed flat shape with three or more straight sides")


class Quadrilateral(Polygon):
    def __init__(self):
        Polygon.__init__(self, 4)

    def description(self):
        print("A quadrilateral is a polygon that has four sides and four angles")


class Triangle(Polygon):
    def description(self):
        print("A triangle is a polygon having 3 sides")

    def __init__(self, a, b, c):
        Polygon.__init__(self, 3)
        self.side1 = a
        self.side2 = b
        self.side3 = c
    
    def Perimeter(self):
        print("Perimeter of triangle = ", self.side1 + self.side2 + self.side3)

    def Area(self):
        #semi_perimeter
        self.s = (self.side1 + self.side2 + self.side3)/2
        self.area = ((self.s)*(self.s - self.side1)*(self.s - self.side2)*(self.s - self.side3))**(0.5)
        print("Area of Triangle = ", self.area)


class EquilateralTriangle(Triangle):
    def description(self):
        print("An Equilateral triangle is a polygon having 3 sides of equal lengths")

    def __init__(self, a):
        Triangle.__init__(self, a,a,a)
        self.side = a

    def DrawTriangle(self):
        et = turtle.Turtle()
        for i in range(3):
            et.forward(self.side)
            et.left(360/3)
        et.clear()


class Square(Quadrilateral):
    def __init__(self, side_length):
        Quadrilateral.__init__(self)
        self.length_of_side = side_length

    def Area(self):
        print("Area of Square = ", self.length_of_side*self.length_of_side)
    
    def Perimeter(self):
        print("Perimeter of Square = ",self.length_of_side*4)

    def DrawSquare(self):
        square = turtle.Turtle()
        for i in range(4):
            square.forward(self.length_of_side) # Forward turtle by length units
            square.left(90) # Turn turtle by 90 degree
        square.clear()
            

class Rectangle(Quadrilateral):
    def __init__(self, length, width):
        Quadrilateral.__init__(self)
        self.length = length
        self.width = width

    def Area(self):
        print("Area of rectangle = ", self.length * self.width)

    def Perimeter(self):
        print("Perimeter of recatngle = ",2 * (self.length +  self.width))

    def DrawRectangle(self):
        rectangle = turtle.Turtle()
        
        #1st side
        rectangle.forward(self.length)
        rectangle.left(90)

        #2nd side
        rectangle.forward(self.width)
        rectangle.left(90)

        #3rd side
        rectangle.forward(self.length)
        rectangle.left(90)

        #4th side
        rectangle.forward(self.width)
        rectangle.left(90)

        rectangle.clear()


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def description(self):
        print("A circle is a 2D shape with a curved edge, so a circle is not a polygon")

    def Area(self):
        print("Area of circle = ", math.pi*self.radius*self.radius)

    def Perimeter(self):
        print("Perimeter of circle = ", 2*math.pi*self.radius)

    def DrawCircle(self):
        c = turtle.Turtle()
        c.circle(self.radius)
        c.clear()


class Octagon(Polygon):
    def __init__(self, length_of_side):
        Polygon.__init__(self, 8)
        self.side = length_of_side
    
    def description(self):
        print("An Octagon is a polygon with 8 sides")
    
    def Area(self):
        print("Area of the regular octagon = ", 2 * self.side * self.side * (1 + 2**0.5))
    
    def Perimeter(self):
        print("Perimeter of the regular octagon = ", 8*self.side)

    def DrawOctagon(self):
        o = turtle.Turtle()
        for i in range(8):
            o.forward(self.side)
            o.left(360/8)
        o.clear()


class Hexagon(Polygon):
    def __init__(self, length_of_side):
        Polygon.__init__(self, 6)
        self.side = length_of_side
    
    def description(self):
        print("An Hexagon is a polygon with 6 sides")
    
    def Area(self):
        print("Area of the regular hexagon = ", 1.5 * self.side * self.side * (3**0.5))
    
    def Perimeter(self):
        print("Perimeter of the regular hexagon = ", 6 * self.side)

    def DrawHexagon(self):
        h = turtle.Turtle()
        for i in range(6):
            h.forward(self.side)
            h.left(360/6)
        h.clear()



s1 = Square(100)
q1 = Quadrilateral()
q1.print_num_sides()
s1.print_num_sides()
s1.Area()
s1.Perimeter()
s1.DrawSquare()


r1 = Rectangle(150,100)
r1.Area()
r1.Perimeter()
r1.DrawRectangle()


c1 = Circle(100)
c1.Perimeter()
c1.Area()
c1.description()
c1.DrawCircle()


t1 = Triangle(4, 3, 5)
t1.description()
t1.print_num_sides()
t1.Area()
t1.Perimeter()


o1 = Octagon(100)
o1.Perimeter()
o1.Area()
o1.description()
o1.DrawOctagon()


h1 = Hexagon(100)
h1.Perimeter()
h1.Area()
h1.description()
h1.DrawHexagon()

eqt = EquilateralTriangle(200)
eqt.DrawTriangle()
eqt.Area()
eqt.Perimeter()
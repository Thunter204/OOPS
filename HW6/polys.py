"""
Author: Toni Hunter
RUID: 187009925
Module for Problem 1, Homework 6

Object Oriented Programming (50:198:113), Spring 2022
implement a Point class, a SimplePoly class, a ConvPoly class, an EquiTriangle class, a Rectangle class,
and a Square class. Instances of the SimplePoly class contain a collection of Point instances. The ConvPoly class
is a sub-class of SimplePoly, the EquiTriangle and Rectangle classes are sub-classes of ConvPoly, and the Square
class is a sub-class of Rectangle.
"""
import math


class Point:
    def __init__(self, x=0, y=0):
        """
        Constructor sets values for coordinates x and y. Default (0,0)
        """
        self.coordx = x
        self.coordy = y

    def translate(self, s, t):
        """
        This method translates the point (x,y) by (s,t).
        """
        self.coordx = self.coordx + s
        self.coordy = self.coordy + t
        return self.coordx, self.coordy

    def rotate(self, degree):
        """
        This method returns coordinates (x*cos(angle) - y*sin(angle),
        x*sin(angle) + y*cos(angle)) in order to rotate by angle about the origin
        """
        degree = math.radians(degree)  # sets angle to radians
        self.coordx = self.coordx * math.cos(degree) - self.coordy * math.sin(degree)
        self.coordy = self.coordx * math.sin(degree) + self.coordy * math.cos(degree)
        return self.coordx, self.coordy

    def distance(self, p):
        """
        This method returns the distance between two points, self and p.
        """
        return math.sqrt(((self.coordx - p.coordx) ** 2) + ((self.coordy - p.coordy) ** 2))

    def left_of(self, q, r):
        """
        This method returns True if the point lies to the left of qr,
        and False otherwise.
        (rxpy − pxry) + (qxry − qxpy) + (qypx − qyrx) > 0.
        """
        num1 = (r.coordx * self.coordy) - (self.coordx * r.coordy)
        num2 = (q.coordx * r.coordy) - (q.coordx * self.coordy)
        num3 = (q.coordy * self.coordx) - (q.coordy * r.coordx)
        if (num1 + num2 + num3) > 0:  # equations put in variables for neatness
            return True
        return False

    def right_of(self, q, r):
        """
        This method returns True if the point lied to the right of qr,
        and False otherwise
        (rxpy −pxry)+ (qxry −qxpy)+ (qypx −qyrx) < 0
        """
        num1 = (r.coordx * self.coordy) - (self.coordx * r.coordy)
        num2 = (q.coordx * r.coordy) - (q.coordx * self.coordy)
        num3 = (q.coordy * self.coordx) - (q.coordy * r.coordx)
        if (num1 + num2 + num3) < 0:
            return True
        return False

    def __str__(self):
        """
        This method returns a string representation of coordinates (x, y)
        """
        return "({},{})".format(self.coordx, self.coordy)

    def __repr__(self):
        return str()


class SimplePoly:
    def __init__(self, *vertices):
        self.vertices = list(vertices)
        self.__count = 0
        self.__length = len(self.vertices)

    def translate(self, s, t):
        """
        This method translates the simple polygon by (s,t)
        """
        for i in self.vertices:
            i.translate(s, t)

    def rotate(self, degree):
        """
        This method rotates the simple polygon by angle.
        """
        degree = math.radians(degree)
        for i in self.vertices:
            i.rotate(degree)

    def __iter__(self):
        """
        This method returns an iterator.
        """
        return self

    def __next__(self):
        """
         This method raises StopIteration
        """
        if self.__count > self.__length - 1:
            raise StopIteration
        else:
            ans = self.vertices[self.__count]  # vertex at index[self.__count]
            self.__count += 1
        return ans

    def __len__(self):
        """
        This method returns the number of vertices in the polygon
        """
        count = 0
        for i in self.vertices:
            count += 1
        return count

    def __getitem__(self, i):
        """
        This method overloads the index operator. returns the i-th vertx of the
        convex polygon, if the index is out of range IndeError is raised.
        """
        if i < 0 or i > len(self.vertices):
            raise IndexError
        return self.vertices[i - 1]

    def __str__(self):
        """
        This method produces a string representation of the polygon.
        """
        point = []
        for i in self.vertices:
            point.append(str(i))
        return ','.join(point)

    def __repr__(self):
        return str(self)

    def perimeter(self):
        """
        This method returns the parameter of the polygon. Use Distance method
        here
        """
        d = 0
        for i in range(len(self.vertices) - 1):
            d += self.vertices[i].distance(self.vertices[i + 1])
        return d + self.vertices[0].distance(self.vertices[-1])


class ConvPoly(SimplePoly):
    def __init__(self, *vertices):
        """
        This method checks if vertices form convex polygon (left turn at each vertex
        in counterclockwise motion)
        """
        # self.vertL = vertices
        for i in range(len(vertices) - 2):
            if vertices[i].right_of(vertices[i + 1], vertices[i + 2]):
                raise Exception("Not a polygon")
        if (vertices[-2].right_of(vertices[-1], vertices[0])) or (vertices[-1].right_of(vertices[0], vertices[1])):
            raise Exception("Not a polygon")

        SimplePoly.__init__(self, *vertices)


class EquiTriangle(ConvPoly):
    def __init__(self, length):
        self.length = length
        ConvPoly.__init__(self, Point(0, 0), Point(self.length, 0),
                          Point(self.length / 2, ((self.length ** 2) - ((self.length / 2) ** 2) ** .5)))

    def area(self):
        """
        This method returns the area of a triangle
        """
        return (math.sqrt(3) / 4) * (self.length ** 2)


class Rectangle(ConvPoly):  # 4 sides on rectangle, 4 set points
    def __init__(self, length, width):
        self.length = length
        self.width = width
        ConvPoly.__init__(self, Point(0, 0), Point(self.length, 0), Point(self.length, self.width), Point(0, self.width))

    def area(self):
        """
        This method returns the area of a rectangle
        """
        return self.length * self.width


class Square(Rectangle):  # same as rectangle
    def __init__(self, length):
        """
        Subclass of Rectangle
        """
        Rectangle.__init__(self, length, length)

import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Circle:
    def __init__(self, x=0, y=0, radius=0):
        self.center = Point(x, y)
        self.radius = radius

    def subtract(self, other):
        if isinstance(other, Circle):
            new_x = self.center.x - other.center.x
            new_y = self.center.y - other.center.y
            new_radius = abs(self.radius - other.radius)
            return Circle(new_x, new_y, new_radius)
        elif isinstance(other, Point):
            new_x = self.center.x - other.x
            new_y = self.center.y - other.y
            return Point(new_x, new_y)
        else:
            raise ValueError("Unsupported type for subtraction")

circle1 = Circle(0, 0, 5)
circle2 = Circle(3, 4, 3)
circle3 = Circle(0, 0, 5)

result_circle = circle1.subtract(circle2)
print("Result Circle - Center: ({}, {}), Radius: {}".format(result_circle.center.x, result_circle.center.y, result_circle.radius))

result_point = circle1.subtract(circle3)
if isinstance(result_point, Point):
    print("Result Point - x: {}, y: {}".format(result_point.x, result_point.y))
else:
    print("Result is not a Point object")

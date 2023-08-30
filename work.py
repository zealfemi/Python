"""Program to calculate distance and slope of a line using class"""

class Line:
    """Class of Line"""
    def __init__(self, coor1, coor2):
        """Initial values""" 
        self.x1 = coor1[0] 
        self.y1 = coor1[1] 
        self.x2 = coor2[0] 
        self.y2 = coor2[1]

    def distance(self):
        """Calculates the distance of the line"""
        return (((self.x2 - self.x1) **2) + ((self.y2 - self.y1) **2))**0.5

    def slope(self):
        """Calculates the slope of the line"""
        return ((self.y2 - self.y1) / (self.x2 - self.x1))
    
coordinate1 = (3,2)
coordinate2 = (8,10)

line = Line(coordinate1, coordinate2)

print(line.distance())
print(line.slope())



"""Calculate volume and surface area of cylinder"""
class Cylinder:
    """Class"""
    pi = 3.14
    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        """Calculates volume"""
        return (Cylinder.pi * (self.radius**2) * self.height)
        
    def surface_area(self):
        """Calculates surface area"""
        return (2 * Cylinder.pi * self.radius * self.height) + (2 * Cylinder.pi * (self.radius**2))
    
c = Cylinder(2,3)

print(c.volume())
print(c.surface_area())
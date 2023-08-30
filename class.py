"""Program to practice class, methods, inheritance class, """

class Circle:
    """Class for Circle"""

    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius
        self.area = 2 * self.radius * Circle.pi

    def circumference(self, number):
        """Calculate the circumference"""
        circumference = self.radius * self.radius * Circle.pi
        return f'Circumference is {circumference} and extra number is {number}'


# my_circle = Circle(18)
# print(my_circle.pi)
# print(my_circle.radius)
# print(my_circle.area)
# print(my_circle.circumference(20))


class Animal:
    """Animal class"""
    def __init__(self):
        print("Animal Created")

    def eat(self):
        """Method"""
        print("I am eating")
    
class Dog(Animal):
    """Inherits Animal class"""
    def __init__(self):
        Animal.__init__(self)
        print("Dog Created")

my_dog = Dog()

print(my_dog.eat())

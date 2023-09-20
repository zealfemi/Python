from collections import namedtuple

d = namedtuple("Dog", "name age color")
mack = d(name= "Mack", age= 5, color= "Brown")

print(mack.name)
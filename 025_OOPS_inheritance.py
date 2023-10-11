class animal:

    alive = True

    def eat():
        print("this animal is eating")
    def sleep():
        print("this animal is sleeing")

class rabbit(animal): # rabbit class is child of animal class 
    def run():
        print("rabbit is running")
class fish(rabbit, animal): # fish has two parents - rabbit as well as animals
    pass

# --------- main ---------
rab1 = rabbit()
print(rab1.alive)
fish.eat()

# multilevel
# multiple
# method overriding

# -----------------------------------------------------------------------------------------------------------------------------------
# method chaining - multiple functions called sequentially where each one (except the last one, which is optional, as it doesnt need to be replaced inside main) returns self
class human:
    
    def height(self):
        print("height")
        return self # self must be defined as a parameter to be used in the return statement

    def weight(self):
        print("weight")
        return self
    
uday = human()
uday.height().weight() # after height is used as a function and gets returned as self - this statement effectively becomes uday.weight()

""" 
    for increased readability

        uday.height()\                                          -----> backslash acts a line continuing character
        .weight()

 """

# -----------------------------------------------------------------------------------------------------------------------------------
# super function
class rectangle:
    def __init__(self, len, bre):
        self.len = len
        self.bre = bre

class square(rectangle):
    def __init__(self, len, bre):
        super().__init__(len, bre) # we directly pass the parameters to the rectangle's constructor
    
    def area(self):
        return self.len*self.bre

class cube(rectangle):
    def __init__(self, len, bre, hei):
        super().__init__(len, bre)
        self.hei = hei
    
    def volume(self):
        return self.len*self.bre*self.hei

sq1 = square(3, 4)
cb1 = cube(3, 4, 5)

print(sq1.area())
print(cb1.volume())

# -----------------------------------------------------------------------------------------------------------------------------------
# abstract class
""" 
    1. prevents a user from creating an object of that class
    2. compels user to override the abstact methods of parent class in the child class

    - abstract class - a class containing any abstract methods
    - abstract methods - method having only declaration and no implementation
"""

from abc import ABC, abstractmethod

class vehicle(ABC):

    # @abstractmethod
    def go(self):
        pass

class car(vehicle):
    def go(self):
        print("you drive the car")

class motorcycle(vehicle):
    def go(self):
        print("you drive the motorcycle")


v1 = vehicle(); # TypeError: Can't instantiate abstract class vehicle with abstract method go
c1 = car();
m1 = motorcycle();

v1.go()
# when the @abstractmethod decorator was present
# TypeError: Can't instantiate abstract class vehicle with abstract method go
c1.go()
m1.go()
""" 
    if      class1 has the same functions as that of class2
    then    an object of class2 can act as an alias to the object of class1

    - duck typing - when class is less important than the object and the methods inside the class
    - "if it walks like a duck and talks like a duck, then it must be a duck"
"""

class class1:
    def walk(self):
        print("class1 is walking")
    def talk(self):
        print("class1 is talking")

class class2:
    def walk(self):
        print("class2 is walking")
    def talk(self):
        print("class2 is talking")

class temp_class:
    def temp_func1(self, class1):                       # class1 object passed and class1 object used
            class1.walk(self)
            class1.talk(self)
            print("temp_func1 of temp_class called")
    def temp_func2(self, class2):                       # class2 object passed but class1 object used - class2 acts as an alias object to the object of class1 - try commenting out one function of the class2 class - which will cause both the classes to have different methods
            class1.walk()
            class1.talk()
            print("temp_func2 of temp_class called")

var1 = temp_class()
cla1 = class1()
cla2 = class2()
var1.temp_func1(class1)
var1.temp_func1(class2)

# --------------------------------------------------------------------------------------------------------------------------------
# walrus opeartor - assigns values to variables as part of a larger expression

# ??????????????????????/////////
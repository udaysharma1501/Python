# if this 'Car' exists as a module inside another file then it can be imported using
    # from file_name import module_name

class Car:

    # class variable - inside the class but outside the constructor - any variables which dont need user initialisation
    wheels = 4 # this can be accessed and changes by an object (ONLY FOR THE OBJECT'S MEMORY)

    def __init__(self, model = None, year = None, color = None): # constructor initialises all the data members
        self.model = model # 'self.' behaves as a this pointer
        self.year = year
        self.color = color

    def start(self): # self - object which calls this method is being passed as an argument
        print("this car is driving")
    def stop(self):
        print("this car has stopped")

# ------------------- main -------------------------
car_1 = Car(12, 1956, "red") # object name = class name(args)
print(car_1.color)
car_1.start(car_1)
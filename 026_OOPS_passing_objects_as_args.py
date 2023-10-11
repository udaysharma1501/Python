class car:
    color = None

def change_color(car, color):
    car.color = color

c1 = car();
c2 = car();
c3 = car();

print(c1.color)
print(c2.color)
print(str(c3.color)+ "\n")

change_color(c1, "blue")

print(c1.color)
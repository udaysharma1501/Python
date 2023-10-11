# str.format() - optional method that gives users more control when displaying output

animal = "neerat"
item = "bananas"
print("the " + animal + " jumped over the " + item)
print()

# cleaner way to insert variables inside printing a string
print("the {} jumped over the {}".format(animal, item)) # positional args
print("the {} jumped over the {}".format("pahul", "paneer sandwich")) 
print()
print("the {0} jumped over the {1}".format("pahul", "paneer sandwich")) 
print("the {1} jumped over the {0}".format("pahul", "paneer sandwich")) # switches placeholders
print()

# keyword args
print("{car1} is faster than {car2}".format(car1="lambo", car2="honda"))
print("{car2} is faster than {car1}".format(car1="lambo", car2="honda"))
print()

# *** indices in positional args and keywords in keyword agrs are reusable within the same string

text = "a {} is slower than {}"
print(text.format("snail", "turtle"))
print()

# padding
print("{} padded text example {:30} example1".format("uday", "sharma"))
print("{} padded text example {:<30} example1".format("uday", "sharma")) # left align
print("{} padded text example {:>30} example1".format("uday", "sharma")) # right align
print("{} padded text example {:^30} example1".format("uday", "sharma")) # center align
print()

# formatting numbers
num = 3.14159
print("pi is {:.2f}".format(num))

num_big = 100000000000000000
print("big num = {:,}".format(num_big))

num_to_other_base = 45
print("binary num = {:b}".format(num_to_other_base))
print("octal num = {:o}".format(num_to_other_base))
print("lowercase hex num = {:x}".format(num_to_other_base))
print("uppercase hex num = {:X}".format(num_to_other_base))
print("uppercase scientific num = {:e}".format(num_to_other_base))
print("lowercase scientific num = {:E}".format(num_to_other_base))
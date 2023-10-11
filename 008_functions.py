# block of code (mini program) which is executed only when called

def print_hello(): # def is a keyword
    print("hello ")

def print_whatever(string_name): # parameter
    print(string_name)

print_hello()
print_hello()
print_hello()

print_whatever("whatever") # arguments can be literals, constants or variables
                           # multiple arguments can also be passed

# return values --------------------------------------------------------------------------------------------------
def multiply(a, b):
    return a*b

print(str(multiply(5, 6))+"\n")

# keyword args --------------------------------------------------------------------------------------------------
# unlike positional args (when the order of passing args matters), keywords can be assigned to each arg to make the order of the arg passing irrelevent

def keywords_arg_example(first, last):
    print("hello " + first +" "+ last)

keywords_arg_example("uday", "sharma")
keywords_arg_example("sharma", "uday")
keywords_arg_example(last="sharma", first="uday") # order doesnt matter, as we've linked specific args to parameters
print()
# nested function calls ---------------------------------------------------------------------------------------
def calc_factorial(num):
    if(num==0):
        return 1
    return num*calc_factorial(num-1)

print(str(calc_factorial(5)))

temp = round(abs(float(input("enter non rounded, non abs number: ")))) # typecasting str to float
print("printing rounded and abs value: "+str(temp))

# --------------------------------------------------------------------------------------------------------------------------------------
# assigning functions to variables

def hello():
    print("hello")

print(hello) # prints function's memory address
hi = hello   # makes an alias to function having the same memory
print(hi)

print()

hi1 = hello
hi1() # alias can directly also be used this way

# alias to built in functions can also be made
cout = print
cout("this is python, not c++ :)")

# --------------------------------------------------------------------------------------------------------------------------------------
# higher order functions
""" 
    functions that either -
        1. accepts a function as an arg
        2. returns a function (in python, functions are treated as objects too)
"""
# example 1:
def caps(text):
    return text.upper()
def lows(text):
    return text.lower()

def hello(func): # function being passed as an arg
    output_text = func("HelLo")
    print(output_text)

hello(caps)
hello(lows)

# example 2:
#   11      /    2    =     5        1
# dividend    divisor   quotient  remainder

def divisor(x):
    def dividend(y):
        return y/x
    return dividend

divide = divisor(2)
print(divide(10))
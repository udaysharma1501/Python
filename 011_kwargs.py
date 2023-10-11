"""
           - key word args ---> kwargs
    kwargs - parameter that will pack all args into a dictionary, instead of a tuple
           - useful so that a function can accept a varying amount of keyword args, instead of positional args
"""
def print1(**dict_name):
    print("hello " + dict_name['first'] +" "+ dict_name['last'])
def print2(**kwargs):
    for key, vals in kwargs.items():
        print(vals, end=" ")

print1(first="uday", last="sharma", middle="amit") # because of kwargs, middle would be ignored

# for no argument to be ignored
print()
print2(first="uday", last="sharma", middle="amit") 
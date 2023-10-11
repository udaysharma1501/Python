# module - header file 
import _021_modules_not_main as add_module

# print(_021_modules_not_main.add(5, 2))
add_module.add(5, 6)

# using 'from module_name import function_name' allows coder to use the function names directly from inside the module without using the object
# 'from module_name import *' imports all functions inside the module

# to get a list of all the modules in python
help("modules")
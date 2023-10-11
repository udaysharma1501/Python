# scoping - LEGB - local, enclosing, global, built in
name = "uday_global"
def print_name():
    name = "uday_local"
    print(name)

def print_name_1():
    print(name)

print_name()
print(name)
print_name_1()
# this closes files automatically after opening and using
with open('C:\\Users\\Uday\\Desktop\\test_for_python.txt') as file_name:
    print(file_name.read())
print()

# print(file_name.read()) # ValueError: I/O operation on closed file.
print(file_name.closed)

# filenotfound errors can be handled using try, except blocks
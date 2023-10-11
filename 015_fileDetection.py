import os

path_variable = "C:\\Users\\Uday\\Desktop\\test_for_python.txt" # manually add backslashes

if os.path.exists(path_variable):

    print("that location exists!")

    if os.path.isfile(path_variable):
        print("this is a file!")
else:
    print("that location doesn't exist!")

print("--------------------------------------------------------------------------------------------------")
path_variable1 = "C:\\Users\\Uday\\Desktop\\test_for_python_folder"

if os.path.exists(path_variable1):

    print("that location exists!")

    if os.path.isfile(path_variable1):
        print("this is a file!")
    elif os.path.isdir(path_variable1):
        print("this is a directory")
else:
    print("that location doesn't exist!")
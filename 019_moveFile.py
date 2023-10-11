import os

# moving 'copy' in project folder to desktop
source_variable      = "E:\\Alternate Desktop\\Code\\Python\\copy.txt"
destination_variable = "E:\\Alternate Desktop\\Code\\copy.txt"

try:
    if os.path.exists(destination_variable):
        print("there is already a file there")
    else:
        os.replace(source_variable, destination_variable)
        print(source_variable + " was moved to " + destination_variable)
except FileNotFoundError:
    print(source_variable + " wasnt found")

# folders can be moved the same way
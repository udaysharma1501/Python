'''
this is a multi-line comment

    collection which is ordered and unchangable
    used to group together related data
'''
student = ("bro", 21, "male")
print(student.count("bro")) # work the same way by returning position
print(student.index("male"))

for x in student:
    print(x)

if "bro" in student:
    print(99)
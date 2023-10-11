# index operator - [] - give access to specific elements from a sequence (string, list, tuple)
name = "udaysharma"

# printing name using for loop and indexing
# for i in range(len(name)):
#     print(name[i], end = "")
# print("\n")

# print all substrings
# u d a y ud da ay uda day uday
# for i in range(0, len(name)+1, 1):
#     for j in range(i, len(name)+1, 1):
#         for counter in range(i, j, 1):
#             print(name[counter], end="")
#         print()


# creating substrings ---------------------------
first_name = name[0:4:1] # 0 1 2 3
print(first_name)

last_name = name[4:len(name):1].upper() # functions can be used directly while doing assingment
print(last_name)

last_char = name[-1]
last_char = name[-1]
print("last character: " + last_char)
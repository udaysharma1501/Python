# stores multiple items in single variable = equivalent of an array in cpp, except that list can hold hetro data

# food = [1, 2, "pizza", 4.2]
# food1 = [2, 5, 1, 99, 12, 1]
# food2 = ["uday", "ria", "max", "bruno"]

# for i in range(0, 4): # for loop equivalent
#     print(food[i])

# for x in food: # for each loop equivalent
#     print(x)

# print(food) # shortcut

# list functions --------------------------------------
# food.append("ice cream")
# food.remove(2)
# food.pop()
# food.insert(0, "cake")
# food.clear()

# food1.sort()
# food2.sort()


# print(food)
# print(food1)
# print(food2)

# --------------------------------2D list--------------------------------

# drinks = ["beer", "coffee"]             # "water"
# snacks = ["hot potato", "fries"]
# dessert = ["gulab jamun", "ice cream"]
# food = [drinks, snacks, dessert]
# print(food)
# print(food[0][1]) # expected 'coffee'

# print("\nprinting as table: ")
# for i in range(3):
#     for j in range (0, 2):
#         print(food[i][j], end=" - ")
#     print()
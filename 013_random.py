import random

x = random.randint(1, 6)
print(x)
print()

y = random.random()
print(y) # random num between 0 and 1
print()

# choosing random item from list
my_list = ['rock', 'paper', 'scissors']
z = random.choice(my_list)
print(z)
print()

cards_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 'J', 'Q', 'K'];
random.shuffle(cards_list);
print(cards_list)
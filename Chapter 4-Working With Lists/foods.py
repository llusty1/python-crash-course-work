# Here we will copy a list 
my_foods = ["pizza", "falafel", "carrot cake"]
friend_foods = my_foods[:] # This makes a copy of my_foods list by using [:]
my_foods.append("cannoli") # Here we add or .append cannoli to my_foods list
friend_foods.append("ice cream") # Here we add or .append ice crean to friend_foods list
print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favcrite foods are:")
print(friend_foods)
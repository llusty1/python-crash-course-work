# Here we will check for Inequality
requested_topping = "mushrooms" # Here is the request

if requested_topping != "anchovies": # If is conditional != means does not equal
    print("Hold the anchovies!")

# Here we will modify the requests
requested_toppings = ["mushrooms", "extra cheese"]

if "mushrooms" in requested_toppings:
    print("Adding mushrooms.")
if "pepperoni" in requested_toppings:
    print("Adding pepperoni.")
if "extra cheese" in requested_toppings:
    print("Adding extra cheese.")
    
print("Finished making your pizza!\n")

# Using if Statements with Lists example later in the chapter.
requested_toppings = ["mushrooms", "green peppers", "extra cheese"]
for requested_topping in requested_toppings:
    if requested_topping == "green peppers":
        print("Sorry we are out of green peppers at this time.")
    else:
        print("Adding " + requested_topping + ".")
print("Finished making your pizza!\n")

# Checking that a list is not empty
requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?\n")

# Using multiple lists
available_toppings = ["mushrooms", "olives", "green peppers", "pepperoni", "pineapple", "extra cheese"]
requested_toppings = ["mushrooms", "fries", "extra cheese"]

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry we don't have " + requested_topping + ".")
print("Finished making your pizza!")
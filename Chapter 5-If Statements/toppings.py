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
    
print("\nFinished making your pizza!\n")

# Using if Statements with Lists example later in the chapter.
requested_toppings = ["mushrooms", "green peppers", "extra cheese"]
for requested_topping in requested_toppings:
    if requested_topping == "green peppers":
        print("Sorry we are out of green peppers at this time.")
    else:
        print("Adding " + requested_topping + ".")
print("\nFinished making your pizza!\n")
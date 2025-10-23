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
    
print("\nFinished making your pizza!")
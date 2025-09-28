# This is a TRY IT YOURSELF exercise 
# Let's make a list of five places we'd like to visit in the world.
print("Here are some places I would like to visit... ")
destinations = ["Japan", "Sweden", "France", "Italy", "Israel"]
print(destinations) # Now print that list.

# Now we will use the sorted() method to print a list in alphabetical order.
print("\nHere is the list in alphabetical order: ")
print(sorted(destinations))

# We will show that the original list isn't altered by using print(destinations)
print("\nAnd here is the original list again:")
print(destinations)

# Now let's reverse the list by using the reverse() method
print("\nHere we print the list in reverse")
destinations.reverse()
print(destinations)

# Let's reverse the list again to show it's unaltered
print("\nI will now magically overwrite the reverse method(), violla:")
destinations.reverse()
print(destinations)

# We will now use sort() method to show the list alphabetically
print("\nAnd now we shall sort() all things out and print it, BOOM:")
destinations.sort()
print(destinations)

# We will use sort() once again to see what has changed
print("\nWith the power invested in me I shall once again use reverse() to change the list again!")
destinations.reverse()
print(destinations)
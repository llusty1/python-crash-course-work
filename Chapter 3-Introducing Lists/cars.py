# This exercise is about sorting a list
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort() # Here we used the sort() method to create an alphabetic list.
cars.sort(reverse=True) # Here we use the reverse argument to alphabetically reverse the list. 
print(cars) 

# Now let's use the sorted() method
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("\nHere is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)

# Now let's print a list in reverse order
cars.reverse()
print(cars)

# Now let's find the length of the list using the len() function.
cars = ["bmw", "audi", "toyota", "subaru"]
print(len(cars)) # Here we print the value of the list by passing the len(cars) within the print() function. 
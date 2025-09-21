# Here we will create another list and then a statement 
# We will focus on motorcycle brands
motorcycle = ['harley davidson panhead', 'honda', 'indian']
message = "I would like to own a " + motorcycle[0].title() + " someday."
print(message)

# Now let's create another list 
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# Now we will change the first element in the list
motorcycles[0] = 'ducati'
print(motorcycles)

# Let's practice adding elements to our list now
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
# Append will add the ducati element to the list of motorcycles
# I can use the append() method to build a list dynamically
motorcycles.append('ducati')
print(motorcycles)

# Let's now use an empty list and add items to it using append()
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)
# Building lists like this is very common.

# Let's learn to insert a new element at any position in a list by using the insert() method.
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati') # The insert() method was put into index position 1
print(motorcycles)

# Removing elements from a list
motorcycles = ['honda', 'yamaha', 'suzuki']
del motorcycles[2] # Using del statement and the position of the element removed it when ran.
print(motorcycles)

# Removing an element using the pop() method
motorcycles = ['honda', 'yamaha', 'suzuki']
popped_motorcycle = motorcycles.pop() # The pop() method removes the last element in a list
print(motorcycles)
print(popped_motorcycle) 
# Removing an element using the pop() method will let you work with that element later on.

# Popping items from any position in a list
motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print("The first motorcycle I owned was a " + first_owned.title() + ".")
# If you can't figure out whether to use the pop() method or the del statement: 
# When you want to delete an item from a list and not use it in any way, use the del statement.
# If you want to use an item as you remove it, use the pop() method. 

# Removing an Item by Value
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati') # Here we used to remove() method 
print(motorcycles)

# Removing an Item by Value - Sometimes you don't know the index position of the value you want to remove.
# The remove() method lets you remove an item from a list by its value.
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
# Now we remove the ducati using .remove() method.
motorcycles.remove('ducati') 
print(motorcycles)

# We can also use the remove() method to work with a value that's being removed from a list. 
# Let's remove the value 'ducati' and print a reason for removing it from the list.
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print("\nA " + too_expensive.title() + " is too expensive for me.")
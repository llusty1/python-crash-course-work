# Example of a list of bicycles
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

# Accessing elements in a list
# The following code uses the position or index of the item desired.
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0]) # The zero represents the index of trek.
print(bicycles[3]) # The 3 represents the index of specialized. 

# We can also use the string method from Chapter 2 on any element in a list. 
# Let's format the element 'trek' more neatly be using the title() method:
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0].title())

# Index Positions Start at 0, Not 1
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[1]) # The 1 represents the index position of cannondale
print(bicycles[3]) # The 3 represents the index position of specialized

# By asking for the item at index -1, Python always returns the last item in the list:
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[-1]) # The -1 represents the last position which is specialized
# This convention extends to other negative index values as well.
# The index -2 returns the second item from the end of the list, the index -3 returns the third item from the end , and so forth.

# Using Individual Values from a List
# Let's try pulling the first bicycle from the list and composing a message using that value.
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)
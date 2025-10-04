# Here we will square numbers
squares = [] # We start with an empty list
for value in range(1,11): # Next we write a for loop using the range() function for 1-11
    square = value**2
    squares.append(square)
print(squares)
# Here is the introduction of List Comprehension
squares = [value**2 for value in range(1,11)]
print(squares)
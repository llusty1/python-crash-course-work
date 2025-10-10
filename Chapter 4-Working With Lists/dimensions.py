# Defining a tuple: Python refers to values that cannot change as immutable, and an immutable list is called a tuple.
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# Looping Trough All Values in a Tuple:
for dimension in dimensions:
    print(dimension)

# Writing Over a Tuple:
print("Original Dimensions: ")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified Dimension: ")
for dimension in dimensions:
    print(dimension)
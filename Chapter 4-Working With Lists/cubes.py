# Here we will cube a list of numbers from 1-10
# We start with an empty list
cubes = []
for value in range(1,11): # Now we create the range
    cube = value**3 
    cubes.append(cube)
print(cubes)
# Here is a list comprehension to show the values of the first 10 cubes
cubes = [value**3 for value in range(1,11)] # Notice there are two * as this problem calls for cubing the numbers. 
print(cubes)